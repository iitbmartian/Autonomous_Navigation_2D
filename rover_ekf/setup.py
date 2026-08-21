from setuptools import find_packages, setup
import os
from glob import glob
package_name = 'rover_ekf'

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
            'dummy_odom_publisher = rover_ekf.dummy_odom_publisher:main',
            'dummy_imu_publisher = rover_ekf.dummy_imu_publisher:main',
            'covariance_relay=rover_ekf.covariance_relay:main',
        ],
    },
)
