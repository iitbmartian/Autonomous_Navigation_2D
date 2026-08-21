import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Imu
class ImuRelay(Node):  
    def __init__(self):
        super().__init__('imu_relay')
        self.subscription = self.create_subscription(
            Imu,
            '/imu1/data',
            self.imu_callback,
            10)
        self.publisher_ = self.create_publisher(Imu, 'imu_relay/data', 10)
        self.get_logger().info('IMU Relay has been started.')

    def imu_callback(self, msg):
        # Relay the incoming IMU message to the new topic
        imu = Imu()
        imu.header = msg.header
        imu.orientation = msg.orientation
        imu.angular_velocity = msg.angular_velocity
        imu.linear_acceleration = msg.linear_acceleration
        imu.orientation_covariance = msg.orientation_covariance
        imu.angular_velocity_covariance = [0.1, 0.0, 0.0,
                                        0.0, 0.1, 0.0,
                                        0.0, 0.0, 0.1]  # Example covariance
        imu.linear_acceleration_covariance = [1.0, 0.0, 0.0,
                                            0.0, 1.0, 0.0,
                                            0.0, 0.0, 1.0]  # Example
        self.publisher_.publish(msg)
        self.get_logger().info('Relayed IMU message.')
def main(args=None):
    rclpy.init(args=args)
    imu_relay = ImuRelay()
    rclpy.spin(imu_relay)
    imu_relay.destroy_node()      
if __name__ == '__main__':    main()