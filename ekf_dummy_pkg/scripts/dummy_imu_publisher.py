import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Imu
import random
class DummyImuPublisher(Node):
    def __init__(self):
        super().__init__('dummy_imu_publisher')
        self.publisher_ = self.create_publisher(Imu, 'imu/data', 10)
        timer_period = 0.01  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.get_logger().info('Dummy IMU Publisher has been started.')

    def timer_callback(self):
        imu_msg = Imu()
        imu_msg.header.stamp = self.get_clock().now().to_msg()
        imu_msg.header.frame_id = 'base_link'
        # Fill in the IMU message with dummy data
        imu_msg.orientation.x = 0.0
        imu_msg.orientation.y = 0.0
        imu_msg.orientation.z = 0.0
        imu_msg.orientation.w = 1.0
        imu_msg.angular_velocity.x = random.gauss(0.0, 0.01)  # Simulate some noise in angular velocity
        imu_msg.angular_velocity.y = random.gauss(0.0, 0.01)  # Simulate some noise in angular velocity
        imu_msg.angular_velocity.z = random.gauss(0.0, 0.01)  # Simulate some noise in angular velocity
        imu_msg.linear_acceleration.x = random.gauss(0.0, 0.05)  # Simulate some noise in linear acceleration
        imu_msg.linear_acceleration.y = random.gauss(0.0, 0.05)  # Simulate some noise in linear acceleration
        imu_msg.linear_acceleration.z = random.gauss(9.81, 0.05)  # Simulate some noise in linear acceleration (gravity)
        imu_msg.angular_velocity_covariance = [0.0000001, 0.0, 0.0,
                                            0.0, 0.0000001, 0.0,
                                            0.0, 0.0, 0.0000001]  # Example covariance
        imu_msg.linear_acceleration_covariance = [0.000025, 0.0, 0.0,
                                                0.0, 0.000025, 0.0,
                                                0.0, 0.0, 0.000025]  # Example covariance
        self.publisher_.publish(imu_msg)
        self.get_logger().info('Published dummy IMU message.')
def main(args=None):
    rclpy.init(args=args)
    dummy_imu_publisher = DummyImuPublisher()
    rclpy.spin(dummy_imu_publisher)
    dummy_imu_publisher.destroy_node()      
if __name__ == '__main__':    main()