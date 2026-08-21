
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Imu
import numpy as np
import time
class dummy_imu(Node):
    def __init__(self):
        super().__init__("dummy_imu_node")
        self.imu_data_pub=self.create_publisher(Imu,"/imu/data",100)
        self.current_time=time.time()
        self.create_timer(0.01,self.timer_callback)
        self.x=0
        self.y=0
        self.velo=0.5

    def timer_callback(self):
        msg=Imu()
        msg.header.frame_id="base_link"
        msg.header.stamp = self.get_clock().now().to_msg()
        ang_noise=np.random.normal(0,0.01)
        msg.angular_velocity.x=0.0+ang_noise
        msg.angular_velocity.y=0.0+ang_noise
        msg.angular_velocity.z=0.0+ang_noise
        lin_accn_noise=np.random.normal(0,0.05)
        msg.linear_acceleration.x=0.0+lin_accn_noise
        msg.linear_acceleration.y=0.0+lin_accn_noise
        msg.linear_acceleration.z=9.81+lin_accn_noise
        msg.angular_velocity_covariance=[
            0.0001,0.0,0.0,
            0.0,0.0001,0.0,
            0.0,0.0,0.0001
        ]
        msg.linear_acceleration_covariance=[
            0.0025,0.0,0.0,
            0.0,0.0025,0.0,
            0.0,0.0,0.0025
        ]
        msg.orientation.x = 0.0
        msg.orientation.y = 0.0
        msg.orientation.z = 0.0
        msg.orientation.w = 1.0
        
        # timenow=time.time()-self.current_time

        self.imu_data_pub.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node=dummy_imu()
    rclpy.spin(node)
    rclpy.shutdown()
if __name__=='__main__':main()