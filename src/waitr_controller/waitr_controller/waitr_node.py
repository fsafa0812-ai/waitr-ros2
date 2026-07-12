import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class WaitRNode(Node):
     def __init__(self):
        super().__init__('waitr_node')
        
        self.subscription = self.create_subscription(String,'customer_order',self.order_callback,10)
        
        self.get_logger().info("WaitR is ready to recieve orders!")

     def order_callback(self,msg):
        self.get_logger().info(f"New Order:{msg.data}")
        
def main(args=None):
   rclpy.init(args=args)
   

   node = WaitRNode()
   rclpy.spin(node)

   node.destroy_node()
   rclpy.shutdown()

if __name__=='__main__':
   main()

