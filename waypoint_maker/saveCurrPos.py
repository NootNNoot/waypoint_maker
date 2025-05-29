import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseWithCovarianceStamped
from rclpy.qos import QoSProfile, QoSReliabilityPolicy, QoSDurabilityPolicy, QoSHistoryPolicy


class PoseSaver(Node):

    def __init__(self):
        super().__init__('pose_saver')

        subscriber_qos = QoSProfile(
            reliability=QoSReliabilityPolicy.RELIABLE,
            history=QoSHistoryPolicy.KEEP_LAST,
            depth=10
        )
        self.sub = self.create_subscription(
            PoseWithCovarianceStamped, 
            'robot1/map_pose',
            self.sub_callback,
            qos_profile=subscriber_qos
        )

        self.file = open("Robot_Poses", 'w')
        self.latest = None

    def sub_callback(self, msg: PoseWithCovarianceStamped):
        self.latest = msg.pose.pose
        
    def run(self):
        try: 
            while rclpy.ok():
                input("Press Enter to Save Robot Pose, Ctrl+C to Exit: ")
                if self.latest:
                    pose = self.latest
                    pose_array = [pose.position.x, pose.position.y, pose.position.z, 
                                pose.orientation.x, pose.orientation.y, pose.orientation.z, pose.orientation.w]
                    file = self.file
                    file.write(f'{pose_array} \n')
                rclpy.spin_once(self, timeout_sec=0.1)
        except KeyboardInterrupt:
            pass




def main(args=None):
    rclpy.init(args=args)


    pose_saver = PoseSaver()

    pose_saver.run()


    pose_saver.file.close()
    pose_saver.destroy_node()
    rclpy.shutdown()
    
if __name__ == "__main__":
    main()


        
