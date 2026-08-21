from launch import LaunchDescription
from launch_ros.actions import Node
import os
from ament_index_python.packages import get_package_share_directory
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():
    pkg_name='rover_gazebosim'
    ekf_pkg_name='rover_ekf'
    # now we will launch each of the launch files and nodes, startin from ekf_dummy
    # then slam_and_rover then nav2_launch, then that twist_to_stamped
    # externally have to launch the controllers after starting the sim

    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(os.path.join(
                get_package_share_directory(ekf_pkg_name),
                'launch',
                'ekf_dummy.launch.py'
            )),
        ),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(os.path.join(
                get_package_share_directory(pkg_name),
                'launch',
                'slam_and_rover.launch.py'
            )),
        ),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(os.path.join(
                get_package_share_directory(pkg_name),
                'launch',
                'nav2_launch.launch.py'
            )),
        ),
        Node(
            package=pkg_name,
            executable='twist_to_stamped',
            name='twist_to_stamped',
            output='screen',
        ),
    ])      