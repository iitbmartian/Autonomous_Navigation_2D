#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Imu
import random

class DummyImuPublisher(Node):
    def __init__(self):
        super().__init__('dummy_imu_publisher')
        # Publish to /imu/data at 100 Hz
        self.publisher = self.create_publisher(Imu, '/imu/data', 10)
        self.timer = self.create_timer(1.0 / 100.0, self.timer_callback)
        
        # Standard deviations from assignment
        self.ang_vel_std = 0.01
        self.lin_acc_std = 0.05

    def timer_callback(self):
        msg = Imu()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = 'base_link'

        # Angular Velocity (0 rad/s + noise)
        msg.angular_velocity.x = random.gauss(0, self.ang_vel_std)
        msg.angular_velocity.y = random.gauss(0, self.ang_vel_std)
        msg.angular_velocity.z = random.gauss(0, self.ang_vel_std)

        # Linear Acceleration (Gravity on Z + noise)
        msg.linear_acceleration.x = random.gauss(0, self.lin_acc_std)
        msg.linear_acceleration.y = random.gauss(0, self.lin_acc_std)
        msg.linear_acceleration.z = random.gauss(9.81, self.lin_acc_std)

        # Covariance Matrices (3x3 flattened arrays, so length 9)
        # Variance = std_dev^2
        ang_var = self.ang_vel_std ** 2  # 0.0001
        lin_var = self.lin_acc_std ** 2  # 0.0025

        # Set diagonals for X [0], Y [4], and Z [8]
        msg.angular_velocity_covariance = [ang_var, 0.0, 0.0, 
                                           0.0, ang_var, 0.0, 
                                           0.0, 0.0, ang_var]

        msg.linear_acceleration_covariance = [lin_var, 0.0, 0.0, 
                                              0.0, lin_var, 0.0, 
                                              0.0, 0.0, lin_var]

        self.publisher.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = DummyImuPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()