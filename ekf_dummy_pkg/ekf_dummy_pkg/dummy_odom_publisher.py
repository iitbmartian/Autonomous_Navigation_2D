import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry
import random
from geometry_msgs.msg import PoseWithCovariance 
from geometry_msgs.msg import TwistWithCovariance
class DummyOdomPublisher(Node):
    def __init__(self):
        self.p_x =0
        super().__init__('dummy_odom_publisher')
        self.publisher_ = self.create_publisher(Odometry, 'odom', 10)
        timer_period = 0.05  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.get_logger().info('Dummy Odom Publisher has been started.')

    def timer_callback(self):
        self.p_x += 0.025
        odom_msg = Odometry()
        odom_msg.header.stamp = self.get_clock().now().to_msg()
        odom_msg.header.frame_id = 'odom'
        odom_msg.child_frame_id = 'base_link'
        # Fill in the odometry message with dummy data
        pose = PoseWithCovariance()
        pose.pose.position.x = random.gauss(self.p_x , (0.05)**0.05)  # Simulate some noise in the position
        pose.pose.position.y = random.gauss(0.0, (0.05)**0.05)  # Simulate some noise in the position
        pose.pose.position.z = 0.0
        pose.pose.orientation.x = 0.0
        pose.pose.orientation.y = 0.0
        pose.pose.orientation.z = 0.0
        pose.pose.orientation.w = 1.0
        pose.covariance = [0.01, 0.0, 0.0, 0.0, 0.0, 0.0,
                           0.0, 0.01, 0.0, 0.0, 0.0, 0.0,
                           0.0, 0.0, 0.01, 0.0, 0.0, 0.0,
                           0.0, 0.0, 0.0, 0.01, 0.0, 0.0,
                           0.0, 0.0, 0.0, 0.0, 0.01, 0.0,
                           0.0, 0.0, 0.0, 0.0, 0.0, 0.01
                           ] # Example covariance
        twist = TwistWithCovariance()
        twist.twist.linear.x = 0.5
        twist.twist.linear.y = 0.0
        twist.twist.linear.z = 0.0
        twist.twist.angular.x = 0.0
        twist.twist.angular.y = 0.0
        twist.twist.angular.z = 0.0
        twist.covariance = [0.01, 0.0, 0.0, 0.0, 0.0, 0.0,
                           0.0, 0.01, 0.0, 0.0, 0.0, 0.0,
                           0.0, 0.0, 0.01, 0.0, 0.0, 0.0,
                           0.0, 0.0, 0.0, 0.01, 0.0, 0.0,
                           0.0, 0.0, 0.0, 0.0, 0.01, 0.0,
                           0.0, 0.0, 0.0, 0.0, 0.0, 0.01
                           ] # Example covariance
        odom_msg.twist = twist  
        odom_msg.pose = pose
        self.publisher_.publish(odom_msg)
        self.get_logger().info('Published dummy odometry message.')
def main(args=None):
    rclpy.init(args=args)
    dummy_odom_publisher = DummyOdomPublisher()
    rclpy.spin(dummy_odom_publisher)
    dummy_odom_publisher.destroy_node()
    rclpy.shutdown()
if __name__ == '__main__':    main()