from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='ex10',
            executable='text_to_cmd_vel',
            name='text_to_cmd_vel',
            output='screen',
            emulate_tty=True,
        ),
    ])
