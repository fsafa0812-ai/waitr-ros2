import rclpy
import time
from rclpy.node import Node
from std_msgs.msg import String


class KitchenNode(Node):

    def __init__(self):
        super().__init__("kitchen_node")

        self.publisher = self.create_publisher(
            String,
            "orders",
            10
        )

        self.get_logger().info("🍳 Kitchen Ready!")

        time.sleep(2)

        orders = [
            "1001,3,Pizza",
            "1002,2,Burger",
            "1003,1,Sushi",
            "1004,4,Pasta",
            "1005,2,Coffee",
        ]
        for order in orders:
            msg = String()
            msg.data = order
            self.publisher.publish(msg)
            self.get_logger().info(f"📤 Sent: {order}")
            time.sleep(2)
    


def main(args=None):
    rclpy.init(args=args)

    node = KitchenNode()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()