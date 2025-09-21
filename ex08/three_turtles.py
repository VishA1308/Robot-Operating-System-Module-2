from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='turtlesim1',
            parameters=[{'background_r': 255, 'background_g': 255, 'background_b': 255}]
        ),
        Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='turtlesim2',
            parameters=[{'background_r': 200, 'background_g': 200, 'background_b': 255}]
        ),
        Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='turtlesim3',
            parameters=[{'background_r': 200, 'background_g': 255, 'background_b': 200}]
        ),
        Node(
            package='turtlesim',
            executable='mimic',
            name='mimic1',
            remappings=[
                ('/input/pose', '/turtle1/pose'),
                ('/output/cmd_vel', '/turtle2/cmd_vel'),
            ]
        ),
        Node(
            package='turtlesim',
            executable='mimic',
            name='mimic2',
            remappings=[
                ('/input/pose', '/turtle2/pose'),
                ('/output/cmd_vel', '/turtle3/cmd_vel'),
            ]
        )
    ])
