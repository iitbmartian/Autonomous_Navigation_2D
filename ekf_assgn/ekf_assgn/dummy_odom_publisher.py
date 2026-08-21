#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry
import random
import math

class DummyOdomPublisher(Node):
    def __init__(self):
        super().__init__('dummy_odom_publisher')
        # Publish to /odom at 20 Hz
        self.publisher = self.create_publisher(Odometry, '/odom', 10)
        self.timer = self.create_timer(1.0 / 20.0, self.timer_callback)
        
        self.x_ideal = 2.0
        self.v_x = 0.5
        self.noise_std_dev = 0.05

    def timer_callback(self):
        msg = Odometry()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = 'odom'
        msg.child_frame_id = 'base_link'

        # Calculate ideal position (distance = velocity * time)
        self.x_ideal += self.v_x * (1.0 / 20.0)

        # Inject noise into position
        msg.pose.pose.position.x = self.x_ideal + random.gauss(0, self.noise_std_dev)
        msg.pose.pose.position.y = random.gauss(0, self.noise_std_dev)

        # Set the velocity
        msg.twist.twist.linear.x = self.v_x

        # Populate Covariance Matrices
        # Index 0 is X variance, Index 7 is Y variance.
        # Variance = std_dev^2 = 0.05^2 = 0.0025
        msg.pose.covariance[0] = 0.0025
        msg.pose.covariance[7] = 0.0025
        
        # We also set a small variance for our velocity to show we trust it
        msg.twist.covariance[0] = 0.0001 

        self.publisher.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = DummyOdomPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()