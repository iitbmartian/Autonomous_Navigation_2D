from launch import LaunchDescription
from launch_ros.actions import Node
import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    pkg_name = 'ekf_assgn' 
    
    ekf_config_path = os.path.join(
        get_package_share_directory(pkg_name),
        'config',
        'ekf_dummy.yaml'
    )

    return LaunchDescription([
        # 1. Start the dummy odometry publisher
        Node(
            package=pkg_name,
            executable='dummy_odom_publisher',
            name='dummy_odom_publisher'
        ),
        
        # 2. Start the EKF node
        Node(
            package='robot_localization',
            executable='ekf_node',
            name='ekf_filter_node',
            parameters=[ekf_config_path]
        ),
        
        # 3. Static transform from map to odom (zero offset/rotation)
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='static_transform_publisher',
            arguments=['0', '0', '0', '0', '0', '0', 'map', 'odom']
        ),

        # 4. Start the dummy IMU publisher
        Node(
            package=pkg_name,
            executable='dummy_imu_publisher',
            name='dummy_imu_publisher'
        ),
    ])