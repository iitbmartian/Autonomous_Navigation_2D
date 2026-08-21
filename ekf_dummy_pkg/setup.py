# from setuptools import find_packages, setup

# package_name = 'ekf_dummy_pkg'

# setup(
#     name=package_name,
#     version='0.0.0',
#     packages=find_packages(exclude=['test']),
#     data_files=[
#         ('share/ament_index/resource_index/packages',
#             ['resource/' + package_name]),
#         ('share/' + package_name, ['package.xml']),
#         ('share/' + package_name + '/launch', ['launch/ekf_dummy.launch.py']),
#         ('share/' + package_name + '/config', ['config/ekf_dummy.yaml']),
#         ('share/' + package_name + '/scripts', ['scripts/dummy_imu_publisher.py']),
#         ('share/' + package_name + '/scripts', ['scripts/odom_relay.py']),
#     ],
#     install_requires=['setuptools'],
#     zip_safe=True,
#     maintainer='pradyun',
#     maintainer_email='pradyunshetty1645@gmail.com',
#     description='TODO: Package description',
#     license='TODO: License declaration',
#     extras_require={
#         'test': [
#             'pytest',
#         ],
#     },
#     entry_points={
#         'console_scripts': [
#             'dummy_odom_publisher= ekf_dummy_pkg.dummy_odom_publisher:main',
#             'dummy_imu_publisher= ekf_dummy_pkg.scripts.dummy_imu_publisher:main',
#             'odom_relay= ekf_dummy_pkg.scripts.odom_relay:main',
#             'imu_relay= ekf_dummy_pkg.imu_relay:main',
#         ],
#     },
# )
from setuptools import find_packages, setup
import os
from glob import glob
package_name = 'ekf_dummy_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),
        (os.path.join('share', package_name, 'config'), glob('config/*.yaml')),
        ('share/' + package_name + '/scripts', ['scripts/dummy_imu_publisher.py']),
        ('share/' + package_name + '/scripts', ['scripts/odom_relay.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='apratim',
    maintainer_email='anand.apratim336@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'dummy_odom_publisher= ekf_dummy_pkg.dummy_odom_publisher:main',
            'dummy_imu_publisher= ekf_dummy_pkg.scripts.dummy_imu_publisher:main',
            'odom_relay= ekf_dummy_pkg.scripts.odom_relay:main',
            'imu_relay= ekf_dummy_pkg.imu_relay:main',
        ],
    },
)
