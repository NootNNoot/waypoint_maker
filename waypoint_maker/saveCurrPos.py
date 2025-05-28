import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseWithCovarianceStamped


class PoseSaver(Node):

    def __init__(self):
        super().__init__('pose_saver')

        self.sub = self.create_subscription(
            PoseWithCovarianceStamped, 
            'robot1/map_pose',
            self.sub_callback
        )

        self.file = open("Robot_Poses", 'w')

    def sub_callback(self, msg: PoseWithCovarianceStamped):
        _ = input("Press Enter to Save Robot Pose: ")
        pose = msg.pose.pose
        pose_array = [pose.position.x, pose.position.y, pose.position.z, 
                      pose.orientation.x, pose.orientation.y, pose.orientation.z, pose.orientation.w]
        file = self.file
        file.write(f'{pose_array}')




def main(args=None):
    rclpy.init(args=args)


    pose_saver = PoseSaver()

    rclpy.spin(pose_saver)


    pose_saver.file.close()
    pose_saver.destroy_node()
    rclpy.shutdown()
    
if __name__ == "__main__":
    main()


        