#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class CommandPublisher(Node):
    def __init__(self):
        super().__init__('command_publisher')
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.get_logger().info('Command Publisher Node has been started.')

    def timer_callback(self):
        msg = Twist()
        msg.linear.x = 0.2 # Forward velocity in m/s
        msg.angular.z = 0.0 #-0.2 # Angular velocity in rad/s
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: linear.x = {msg.linear.x}, angular.z = {msg.angular.z}')

def main(args=None):
    rclpy.init(args=args)
    node = CommandPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
