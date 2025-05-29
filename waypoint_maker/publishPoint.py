import rclpy
from geometry_msgs.msg import PoseStamped, PoseWithCovarianceStamped
from rclpy.node import Node
from rclpy.duration import Duration
import time




class PointPublish(Node):
    def __init__(self):
        super().__init__('point_publisher')
        self.goal = ...

        self.pub = self.create_publisher(PoseStamped, 'robot1/goal_pose', 10)
        self.file = open("Robot_Poses", 'r')
        self.points = self.create_point_dict()
        self.file.close()
        self.timer = self.create_timer(0.5, self.enter_check)

    def enter_check(self):
        try:
            self.goal = input("Enter a goal number (An example would be 0 or 3): ")
            self.timer_callback()
        except:
            pass

    def timer_callback(self):
        if self.goal == "":
            return
        
        print("In Callback")
        print(self.goal)
        

        pose = self.points[f'goal {self.goal}']
        print(pose)
        goal_pose = PoseStamped()
        goal_pose.header.frame_id = 'map'
        goal_pose.header.stamp = self.get_clock().now().to_msg()
        goal_pose.pose.position.x = float(pose[0])
        goal_pose.pose.position.z = float(pose[2])
        goal_pose.pose.position.y = float(pose[1])
        goal_pose.pose.orientation.x = float(pose[3])
        goal_pose.pose.orientation.y = float(pose[4])
        goal_pose.pose.orientation.z = float(pose[5])
        goal_pose.pose.orientation.w = float(pose[6])
        print(goal_pose)
        self.pub.publish(goal_pose)
    

    def create_point_dict(self):
        dict = {}
        iter = 0
        for line in self.file:
            arr = []
            for num in line.strip()[1:-2].split(','):
                arr.append(float(num))
            
            dict[f'goal {iter}'] = arr
            iter += 1

        return dict


def main(args=None):
    rclpy.init(args=args)

    point_publisher = PointPublish()

    rclpy.spin(point_publisher)

    point_publisher.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()
