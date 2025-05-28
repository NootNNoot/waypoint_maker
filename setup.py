from setuptools import find_packages, setup

package_name = 'waypoint_maker'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Kacper',
    maintainer_email='kacpergasior19@gmail.com',
    description='Saving and publishing positions of MP-400 neobotix robot to use waypoints',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'save_pose = waypoint_maker.saveCurrPos:main',
            'go_to_goal = waypoint_maker.publishPoint:main'
        ],
    },
)
