#!/usr/bin/env python3
import rclpy
import asyncio
import openai
from openai import OpenAI
import cv2
import base64
import numpy as np
from rclpy.node import Node
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
import math
import time
import sys  # To read command-line arguments
from rich.console import Console
from rich.text import Text

# OpenAI API Key (Replace with your own key)
import os
api_key = os.getenv("OPENAI_API_KEY")
console = Console()

class RobotController(Node):
    """ROS 2 Node for publishing velocity commands with predefined movement functions"""
    
    def __init__(self):
        super().__init__('robot_controller')
        self.pub = self.create_publisher(Twist, '/cmd_vel', 10)
        self.current_velocity = Twist()
        
        # Subscribe to Odometry to track position
        self.sub = self.create_subscription(Odometry, '/odom', self.odometry_callback, 10)
        self.pose = None  # Store robot's position
        self.yaw = None   # Store robot's orientation (yaw angle)

        self.command = sys.argv[1] if len(sys.argv) > 1 else "Assess the environment and select an appropriate action."
        self.get_logger().info(f"Using command: {self.command}")
        
        # Timer for publishing velocity at 10Hz
        self.create_timer(0.1, self.publish_velocity)  
        
        # Start querying OpenAI asynchronously
        self.loop = asyncio.get_event_loop()
        self.loop.create_task(self.query_openai_decision())

        self.get_logger().info("RobotController initialized with predefined movements.")

    def odometry_callback(self, msg):
        """Updates robot's pose from odometry"""
        self.pose = msg.pose.pose.position
        orientation_q = msg.pose.pose.orientation
        _, _, self.yaw = self.euler_from_quaternion(orientation_q)

    def euler_from_quaternion(self, quaternion):
        """Converts quaternion to euler angles"""
        x, y, z, w = quaternion.x, quaternion.y, quaternion.z, quaternion.w
        t3 = 2.0 * (w * z + x * y)
        t4 = 1.0 - 2.0 * (y * y + z * z)
        return 0.0, 0.0, math.atan2(t3, t4)  # Return only yaw angle

    def publish_velocity(self):
        """Publish the current velocity command"""
        self.pub.publish(self.current_velocity)

    def stop(self):
        """Stops the robot."""
        self.current_velocity.linear.x = 0.0
        self.current_velocity.angular.z = 0.0
        self.pub.publish(self.current_velocity)
        self.get_logger().info("Robot stopped.")

    def move_forward(self, distance, speed=0.2):
        """Moves forward by a specified distance (meters)."""
        if self.pose is None:
            self.get_logger().warn("Odometry not available.")
            return

        start_x, start_y = self.pose.x, self.pose.y
        traveled_distance = 0

        while traveled_distance < distance:
            self.current_velocity.linear.x = speed
            self.current_velocity.angular.z = 0.0
            self.pub.publish(self.current_velocity)
            time.sleep(0.1)  # Small delay for control loop

            # Update traveled distance
            traveled_distance = math.sqrt(
                (self.pose.x - start_x) ** 2 + (self.pose.y - start_y) ** 2
            )

        self.stop()
        self.get_logger().info(f"Moved forward {distance} meters.")

    def turn(self, angle, speed=0.2):
        """Turns the robot by a specified angle (degrees)."""
        if self.yaw is None:
            self.get_logger().warn("Odometry not available.")
            return

        initial_yaw = self.yaw
        target_yaw = initial_yaw + math.radians(angle)
        target_yaw = (target_yaw + math.pi) % (2 * math.pi) - math.pi  # Normalize angle

        if angle > 0:
            self.current_velocity.angular.z = abs(speed)  # Turn left
        else:
            self.current_velocity.angular.z = -abs(speed)  # Turn right

        while abs(self.yaw - target_yaw) > 0.02:  # Small tolerance for stopping
            self.pub.publish(self.current_velocity)
            time.sleep(0.1)

        self.stop()
        self.get_logger().info(f"Turned {angle} degrees.")

    def capture_frame(self):
        """Captures a frame from the camera, displays it in real-time, and encodes it in base64."""
        cap = cv2.VideoCapture(0)  # Use GStreamer pipeline if needed for CSI cameras
        ret, frame = cap.read()
        cap.release()

        if not ret:
            self.get_logger().warn("Failed to capture image.")
            return None
        
        frame = cv2.resize(frame, (320,240)) # Reduce image size for faster transmission
        cv2.imshow("Robot Camera View", frame)
        cv2.waitKey(1)  # Allow OpenCV to update the window

        _, buffer = cv2.imencode('.jpg', frame)  # Encode frame as JPEG
        return base64.b64encode(buffer).decode('utf-8')  # Convert to base64 string

    async def query_openai_decision(self):
        """Queries OpenAI to decide movement based on image and command."""
        openai.api_key = api_key
        client = OpenAI(api_key=api_key)

        while rclpy.ok():
            base64_image = self.capture_frame()
            if base64_image is None:
                await asyncio.sleep(5)  # Wait before retrying
                continue  

            prompt = f"You are controlling a robot to achieve following sequence: {self.command}. The image is from your front camera and you might be middle of the mission, select your action from 'forward', 'turn right', 'turn left', 'stop'. Only reply the action."

            try:
                response = await asyncio.to_thread(client.chat.completions.create,
                    model="gpt-4o",
                    messages=[
                        {
                            "role": "user",
                            "content": [
                                {"type": "text", "text": prompt},
                                {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}}
                            ],
                        }
                    ]
                )

                decision = response.choices[0].message.content.strip().lower()
                self.get_logger().info(f"OpenAI decision: {decision}")

                # Execute predefined movements
                if "forward" in decision:
                    self.move_forward(1.0)  # Move forward 1 meter
                elif "turn right" in decision:
                    self.turn(-90)  # Turn 90° right
                elif "turn left" in decision:
                    self.turn(90)  # Turn 90° left
                elif "stop" in decision:
                    self.stop()
                else:
                    self.get_logger().warn("Invalid response from OpenAI. Stopping the robot.")
                    self.stop()

            except Exception as e:
                self.get_logger().error(f"OpenAI API request failed: {str(e)}")
                self.stop()

            await asyncio.sleep(5)  # Adjust based on response time

async def main():
    """Initialize and run the ROS 2 node with asyncio handling."""
    rclpy.init()
    robot_controller = RobotController()

    executor = rclpy.executors.MultiThreadedExecutor()
    executor.add_node(robot_controller)

    loop = asyncio.get_running_loop()
    ros_task = loop.run_in_executor(None, executor.spin)

    try:
        await ros_task
    except KeyboardInterrupt:
        pass
    finally:
        robot_controller.destroy_node()
        rclpy.shutdown()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    asyncio.run(main())
