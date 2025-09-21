#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from geometry_msgs.msg import Twist

class TextToCmdVel(Node):
    def __init__(self):
        super().__init__('text_to_cmd_vel')
        
        # Подписка на текстовые команды
        self.subscription = self.create_subscription(
            String,
            'cmd_text',
            self.cmd_text_callback,
            10)
        self.subscription  # предотвращение предупреждения о неиспользуемой переменной
        
        # Публикация команд скорости
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        
        self.get_logger().info('Text to cmd_vel node started')
        self.get_logger().info('Listening for commands: "turn_right", "turn_left", "move_forward", "move_backward"')

    def cmd_text_callback(self, msg):
        command = msg.data.lower().strip()
        self.get_logger().info(f'Received command: "{command}"')
        
        twist_msg = Twist()
        
        # Обработка различных команд
        if command == 'turn_right':
            twist_msg.angular.z = -1.5  # Поворот вправо (отрицательное значение)
            self.get_logger().info('Turning right')
            
        elif command == 'turn_left':
            twist_msg.angular.z = 1.5   # Поворот влево (положительное значение)
            self.get_logger().info('Turning left')
            
        elif command == 'move_forward':
            twist_msg.linear.x = 1.0    # Движение вперед
            self.get_logger().info('Moving forward')
            
        elif command == 'move_backward':
            twist_msg.linear.x = -1.0   # Движение назад
            self.get_logger().info('Moving backward')
            
        else:
            self.get_logger().warn(f'Unknown command: "{command}"')
            return
        
        # Публикация команды скорости
        self.publisher_.publish(twist_msg)
        self.get_logger().info('Published velocity command')

def main(args=None):
    rclpy.init(args=args)
    
    text_to_cmd_vel = TextToCmdVel()
    
    try:
        rclpy.spin(text_to_cmd_vel)
    except KeyboardInterrupt:
        pass
    finally:
        text_to_cmd_vel.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
