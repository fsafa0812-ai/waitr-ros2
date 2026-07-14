import rclpy
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

        self.timer = self.create_timer(5.0, self.send_order)

        self.order_sent = False

        self.get_logger().info("🍳 Kitchen Ready!")

    def send_order(self):

        if self.order_sent:
            return

        msg = String()
        msg.data = "1001,3,Pizza"

        self.publisher.publish(msg)

        self.get_logger().info(f"📤 Sent: {msg.data}")

        self.order_sent = True


def main(args=None):
    rclpy.init(args=args)

    node = KitchenNode()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()