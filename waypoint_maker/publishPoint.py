import rclpy
import time 
from geometry_msgs.msg import PoseStamped, PoseWithCovarianceStamped
from rclpy.node import Node
from rclpy.duration import Duration
import rclpy.time



class PointPublish(Node):
    def __init__(self):
        super().__init__('point_publisher')
        self.goal
        self.pub = self.create_publisher(PoseStamped, 'robot1/goal_pose', 10)
        self.file = open("Robot_Poses", 'r')
        self.points = self.create_point_dict()
        self.file.close()
        self.timer = self.create_timer(0.1, self.enter_check)

    def enter_check(self):
        try:
            self.goal = input("Enter a goal number (An example would be 0 or 3): ")
            self.timer_callback()
        except:
            pass

    def timer_callback(self):
        if self.goal >= len(self.point):
            raise ValueError("Goal Index Out of Range")
        pose = self.points[f'goal {self.goal}']
        goal_pose = PoseStamped()
        goal_pose.header.frame_id = 'map'
        goal_pose.header.stamp = Node.get_clock().now()
        goal_pose.pose.position.x = pose[0]
        goal_pose.pose.position.z = pose[2]
        goal_pose.pose.position.y = pose[1]
        goal_pose.pose.orientation.x = pose[3]
        goal_pose.pose.orientation.y = pose[4]
        goal_pose.pose.orientation.z = pose[5]
        goal_pose.pose.orientation.w = pose[6]
        self.pub.publish(goal_pose)
    

    def create_point_dict(self):
        dict = {}
        iter = 0
        for line in self.file:
            arr = []
            for num in line[1:-2].split(','):
                arr.append(num)
            
            dict[f'goal {iter}'] = arr
            iter += 1

        return dict


