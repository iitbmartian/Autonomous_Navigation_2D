from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
import os
from ament_index_python.packages import get_package_share_directory
def generate_launch_description():
    return LaunchDescription([
        # IncludeLaunchDescription(
        #     PythonLaunchDescriptionSource(os.path.join(get_package_share_directory('rover_gazebosim'), 'launch', 'spawn_rover.launch.py'))),
        Node(
            package='robot_localization',
            executable='ekf_node',
            name='ekf_node',
            output='screen',
            parameters=[os.path.join(get_package_share_directory('ekf_dummy_pkg'), 'config', 'ekf_dummy.yaml'),{'use_sim_time': True}]
        ),
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='map_to_odom_tf',
            arguments=['0', '0', '0', '0', '0', '0', 'map', 'odom'],
            output='screen',
            parameters=[{'use_sim_time': True}]
        ),
        Node(
            package='ekf_dummy_pkg',
            executable='dummy_odom_publisher',
            name='odom_relay',
            output='screen',
            parameters=[{'use_sim_time': True}]
        ),
        Node(
            package='ekf_dummy_pkg',
            executable='dummy_imu_publisher',
            name='imu_relay',
            output='screen',
            parameters=[{'use_sim_time': True}]
        )
    ])