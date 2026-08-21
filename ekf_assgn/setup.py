from setuptools import find_packages, setup
from glob import glob
import os

package_name = 'ekf_assgn'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/ekf_assgn']),
        ('share/ekf_assgn', ['package.xml']),
        (os.path.join('share', 'ekf_assgn', 'launch'), glob('launch/*.launch.py')),
        (os.path.join('share', 'ekf_assgn', 'config'), glob('config/*.yaml')),  # <-- Add this line
    ],  
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='sohan',
    maintainer_email='sohan.chelekar@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'dummy_odom_publisher = ekf_assgn.dummy_odom_publisher:main',
            'dummy_imu_publisher = ekf_assgn.dummy_imu_publisher:main',
            'covariance_relay = ekf_assgn.covariance_relay:main',
        ],
    },
)

