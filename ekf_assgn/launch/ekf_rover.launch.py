from launch import LaunchDescription
from launch_ros.actions import Node
import os
from ament_index_python.packages import get_package_share_directory
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():
    pkg_name = 'ekf_assgn' 
    
    ekf_config_path = os.path.join(
        get_package_share_directory(pkg_name),
        'config',
        'ekf_rover.yaml'
    )
    rover_launch_path = os.path.join(
        get_package_share_directory('rover_gazebosim'),
        'launch',
    )

    return LaunchDescription([
        IncludeLaunchDescription(
             PythonLaunchDescriptionSource(rover_launch_path)
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

        Node(
            package=pkg_name,  
            executable='covariance_relay',
            name='covariance_relay',
            output='screen'
        ),
    ])