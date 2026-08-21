import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry
import numpy as np
import time
class dummy_odom(Node):
    def __init__(self):
        super().__init__("dummy_odom_node")
        self.odo_data_pub = self.create_publisher(Odometry, "/odom", 40)
        self.last_time = self.get_clock().now()
        self.create_timer(0.05, self.timer_callback)
        self.x = 0.0
        self.y = 0.0
        self.velo = 0.5

    def timer_callback(self):
        msg=Odometry()
        noisex=np.random.normal(0,0.05)
        noisey=np.random.normal(0,0.05)
        # timenow=time.time()-self.current_time
        now = self.get_clock().now()
        dt = (now.nanoseconds - self.last_time.nanoseconds) * 1e-9
        if dt <= 0.0:
            dt = 0.05
        self.last_time = now

        self.x += self.velo * dt
        self.y += 0.0 * dt

        msg.header.stamp = now.to_msg()
        msg.header.frame_id = "odom"
        msg.child_frame_id="base_link"
        msg.pose.pose.position.x=self.x+noisex
        msg.pose.pose.position.y=self.y+noisey
        msg.twist.twist.linear.x=self.velo
        msg.pose.covariance=[
            0.0025,0.0,0.0,0.0,0.0,0.0,
            0.0,0.0025,0.0,0.0,0.0,0.0,
            0.0,0.0,0.0025,0.0,0.0,0.0,
            0.0,0.0,0.0,0.0025,0.0,0.0,
            0.0,0.0,0.0,0.0,0.0025,0.0,
            0.0,0.0,0.0,0.0,0.0,0.0025

        ]

        msg.twist.covariance=[
            0.0025,0.0,0.0,0.0,0.0,0.0,
            0.0,0.0025,0.0,0.0,0.0,0.0,
            0.0,0.0,0.0025,0.0,0.0,0.0,
            0.0,0.0,0.0,0.0025,0.0,0.0,
            0.0,0.0,0.0,0.0,0.0025,0.0,
            0.0,0.0,0.0,0.0,0.0,0.0025

        ]
        msg.pose.pose.orientation.x=0.0
        msg.pose.pose.orientation.y=0.0
        msg.pose.pose.orientation.z=0.0
        msg.pose.pose.orientation.w=1.0
        
        
        
        self.odo_data_pub.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node=dummy_odom()
    rclpy.spin(node)
    rclpy.shutdown()
if __name__=='__main__':main()


# import rclpy
# from rclpy.node import Node
# from nav_msgs.msg import Odometry
# import random
# from geometry_msgs.msg import PoseWithCovariance 
# from geometry_msgs.msg import TwistWithCovariance
# class DummyOdomPublisher(Node):
#     def __init__(self):
#         self.p_x =0
#         super().__init__('dummy_odom_publisher')
#         self.publisher_ = self.create_publisher(Odometry, 'odom', 10)
#         timer_period = 0.05  # seconds
#         self.timer = self.create_timer(timer_period, self.timer_callback)
#         self.get_logger().info('Dummy Odom Publisher has been started.')

#     def timer_callback(self):
#         self.p_x += 0.025
#         odom_msg = Odometry()
#         odom_msg.header.stamp = self.get_clock().now().to_msg()
#         odom_msg.header.frame_id = 'odom'
#         odom_msg.child_frame_id = 'base_link'
#         # Fill in the odometry message with dummy data
#         pose = PoseWithCovariance()
#         pose.pose.position.x = random.gauss(self.p_x , (0.05)**0.05)  # Simulate some noise in the position
#         pose.pose.position.y = random.gauss(0.0, (0.05)**0.05)  # Simulate some noise in the position
#         pose.pose.position.z = 0.0
#         pose.pose.orientation.x = 0.0
#         pose.pose.orientation.y = 0.0
#         pose.pose.orientation.z = 0.0
#         pose.pose.orientation.w = 1.0
#         pose.covariance = [0.01, 0.0, 0.0, 0.0, 0.0, 0.0,
#                            0.0, 0.01, 0.0, 0.0, 0.0, 0.0,
#                            0.0, 0.0, 0.01, 0.0, 0.0, 0.0,
#                            0.0, 0.0, 0.0, 0.01, 0.0, 0.0,
#                            0.0, 0.0, 0.0, 0.0, 0.01, 0.0,
#                            0.0, 0.0, 0.0, 0.0, 0.0, 0.01
#                            ] # Example covariance
#         twist = TwistWithCovariance()
#         twist.twist.linear.x = 0.5
#         twist.twist.linear.y = 0.0
#         twist.twist.linear.z = 0.0
#         twist.twist.angular.x = 0.0
#         twist.twist.angular.y = 0.0
#         twist.twist.angular.z = 0.0
#         twist.covariance = [0.01, 0.0, 0.0, 0.0, 0.0, 0.0,
#                            0.0, 0.01, 0.0, 0.0, 0.0, 0.0,
#                            0.0, 0.0, 0.01, 0.0, 0.0, 0.0,
#                            0.0, 0.0, 0.0, 0.01, 0.0, 0.0,
#                            0.0, 0.0, 0.0, 0.0, 0.01, 0.0,
#                            0.0, 0.0, 0.0, 0.0, 0.0, 0.01
#                            ] # Example covariance
#         odom_msg.twist = twist  
#         odom_msg.pose = pose
#         self.publisher_.publish(odom_msg)
#         self.get_logger().info('Published dummy odometry message.')
# def main(args=None):
#     rclpy.init(args=args)
#     dummy_odom_publisher = DummyOdomPublisher()
#     rclpy.spin(dummy_odom_publisher)
#     dummy_odom_publisher.destroy_node()
#     rclpy.shutdown()
# if __name__ == '__main__':    main()