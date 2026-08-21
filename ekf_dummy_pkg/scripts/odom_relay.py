import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry
import random
from rclpy.qos import qos_profile_sensor_data
class OdomRelay(Node):
    def __init__(self):
        super().__init__('odom_relay')
        self.subscription = self.create_subscription(
            Odometry,
            '/odom1',
            self.odom_callback,
            qos_profile_sensor_data )
        self.publisher_ = self.create_publisher(Odometry, 'odom2', 10)
        self.get_logger().info('Odom Relay has been started.')

    def odom_callback(self, msg):
        # Here you can modify the message if needed before relaying
        relay = Odometry()
        relay.header.frame_id = 'odom'
        relay.child_frame_id = 'base_link'
        relay.header.stamp = msg.header.stamp
        relay.pose.pose.position.x = random.gauss(msg.pose.pose.position.x,0.1)
        relay.pose.pose.position.y = random.gauss(msg.pose.pose.position.y,0.1)
        relay.pose.pose.position.z = msg.pose.pose.position.z
        relay.pose.pose.orientation = msg.pose.pose.orientation
        relay.pose.covariance = [0.01, 0.0, 0.0, 0.0, 0.0, 0.0,
                                0.0, 0.01, 0.0, 0.0, 0.0, 0.0,
                                0.0, 0.0, 0.01, 0.0, 0.0, 0.0,
                                0.0, 0.0, 0.0, 0.01, 0.0, 0.0,
                                0.0, 0.0, 0.0, 0.0, 0.01, 0.0,
                                0.0, 0.0, 0.0, 0.0, 0.0, 0.01
                                ]
        relay.twist.twist = msg.twist.twist
        relay.twist.covariance = [0.01, 0.0, 0.0, 0.0, 0.0, 0.0,
                                0.0, 0.01, 0.0, 0.0, 0.0, 0.0,
                                0.0, 0.0, 0.01, 0.0, 0.0, 0.0,
                                0.0, 0.0, 0.0, 0.01, 0.0, 0.0,
                                0.0, 0.0, 0.0, 0.0, 0.01, 0.0,
                                0.0, 0.0, 0.0, 0.0, 0.01, 0.0
                                ]
        self.publisher_.publish(relay)
        self.get_logger().info('Relayed odometry message.')
def main(args=None):
    rclpy.init(args=args)
    odom_relay = OdomRelay()
    rclpy.spin(odom_relay)
    odom_relay.destroy_node()    
if __name__ == '__main__':    main()