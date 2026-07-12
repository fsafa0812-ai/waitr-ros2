import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class KitchenNode(Node):
    def __init__(self):
        super().__init__('kitchen_node')
        self.publisher = self.create_publisher(String,'customer_order',10)
        self.timer = self.create_timer(2.0,self.send_order)

        self.get_logger().info("Kitchen is Ready !")
    def send_order(self) :
        msg=String()
        msg.data="Order for Table 3"
        self.publisher.publish(msg)
        self.get_logger().info(f"Sent:{msg.data}")
def main(args=None):
        rclpy.init(args=args)
        node = KitchenNode()

        rclpy.spin_once(node)
        node.destroy_node()
        rclpy.shutdown()
if __name__=='__main__':
         main()
