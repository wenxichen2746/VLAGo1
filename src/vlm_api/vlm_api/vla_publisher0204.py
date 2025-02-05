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
import sys  # To read command-line arguments
from rich.console import Console
from rich.text import Text

# OpenAI API Key (Replace with your own key)
import os
api_key = os.getenv("OPENAI_API_KEY")
console = Console()

class RobotController(Node):
    """ROS 2 Node for publishing velocity commands"""
    def __init__(self):
        super().__init__('robot_controller')
        self.pub = self.create_publisher(Twist, '/cmd_vel', 10)
        self.current_velocity = Twist()
        self.command = sys.argv[1] if len(sys.argv) > 1 else "Assess the environment and select an appropriate action."
        self.get_logger().info(f"Using command: {self.command}")
        
        # Timer for publishing velocity at 10Hz
        self.create_timer(0.1, self.publish_velocity)  
        
        # Start querying OpenAI asynchronously
        self.loop = asyncio.get_event_loop()
        self.loop.create_task(self.query_openai_decision())

    def publish_velocity(self):
        """Publish the current velocity command"""
        self.pub.publish(self.current_velocity)
        return

    def capture_frame(self):
        """Captures a frame from the camera, displays it in real-time, and encodes it in base64."""
        cap = cv2.VideoCapture(0)  # Use GStreamer pipeline if needed for CSI cameras
        ret, frame = cap.read()
        cap.release()

        if not ret:
            self.get_logger().warn("Failed to capture image.")
            return None
        
        # Display the captured image
        cv2.imshow("Robot Camera View", frame)
        cv2.waitKey(1)  # Allow OpenCV to update the window

        _, buffer = cv2.imencode('.jpg', frame)  # Encode frame as JPEG
        return base64.b64encode(buffer).decode('utf-8')  # Convert to base64 string

    async def query_openai_decision(self):
        """Queries OpenAI to decide movement based on image and command."""
        openai.api_key = api_key  # Ensure your API key is set
        client = OpenAI(api_key=api_key)
        
        while rclpy.ok():
            # Capture and display the latest image
            base64_image = self.capture_frame()
            if base64_image is None:
                await asyncio.sleep(5)  # Wait before retrying
                continue  

            # Define the prompt
            prompt = f"You are controlling a robot to achieve following sequence: {self.command}. The image is from your front camera and you might be middle of the mission, select your action from 'forward', 'turn right', 'turn left', 'stop'. Only reply the action."

            try:
                # Send request to OpenAI using new format
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
                    ],
                    logprobs=True, 
                    top_logprobs=5
                )

                decision = response.choices[0].message.content.strip().lower()
                self.get_logger().info(f"OpenAI decision: {decision}")

                # Update velocity command based on decision
                if "forward" in decision:
                    self.current_velocity.linear.x = 0.2
                    self.current_velocity.angular.z = 0.0
                elif "turn right" in decision:
                    self.current_velocity.linear.x = 0.0
                    self.current_velocity.angular.z = -0.3
                elif "turn left" in decision:
                    self.current_velocity.linear.x = 0.0
                    self.current_velocity.angular.z = 0.3
                elif "stop" in decision:
                    self.current_velocity.linear.x = 0.0
                    self.current_velocity.angular.z = 0.0
                else:
                    self.get_logger().warn("Invalid response from OpenAI. Stopping the robot.")
                    self.current_velocity.linear.x = 0.0
                    self.current_velocity.angular.z = 0.0
                
            except Exception as e:
                self.get_logger().error(f"OpenAI API request failed: {str(e)}")
            
            await asyncio.sleep(5)  # Adjust based on response time

async def main():
    """Initialize and run the ROS 2 node with proper asyncio handling."""
    rclpy.init()
    robot_controller = RobotController()

    # Run ROS 2 node and OpenAI queries concurrently
    executor = rclpy.executors.MultiThreadedExecutor()
    executor.add_node(robot_controller)

    # Run both ROS 2 and asyncio loop together
    loop = asyncio.get_running_loop()
    ros_task = loop.run_in_executor(None, executor.spin)
    
    try:
        await ros_task
    except KeyboardInterrupt:
        pass
    finally:
        robot_controller.destroy_node()
        rclpy.shutdown()
        cv2.destroyAllWindows()  # Close OpenCV windows

if __name__ == '__main__':
    asyncio.run(main())
 
 