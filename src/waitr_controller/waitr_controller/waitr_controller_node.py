import rclpy
from rclpy.node import Node

from .order import Order
from .order_manager import OrderManager
from .state_machine import StateMachine, RobotState
from std_msgs.msg import String

class WaitRController(Node):

    def __init__(self):
        super().__init__("waitr_controller")
        
        self.order_manager = OrderManager()
        self.state_machine = StateMachine()

        self.get_logger().info("🤖 WaitR Controller Started-VERSION 2")
        print("DEBUG:Subscriber is being created")
        
        self.subscription = self.create_subscription(
            String,
            "orders",
            self.order_callback,
            10
        )
    

    def process_order(self, order):
        self.order_manager.add_order(order)

    def serve_orders(self):
        def serve_orders(self):
    while self.order_manager.pending_orders() > 0:

        order = self.order_manager.get_next_order()

        self.get_logger().info( f"🚀 Serving Order #{order.order_id}" )

        self.get_logger().info("🏠 Going to Kitchen")
        self.state_machine.change_state(RobotState.GO_TO_KITCHEN)

        self.get_logger().info(f"🍕 Picking {order.items[0]}")
        self.state_machine.change_state(RobotState.PICK_FOOD)

        self.get_logger().info(f"🧭 Navigating to Table {order.table_number}")
        self.state_machine.change_state(RobotState.GO_TO_TABLE)

        self.get_logger().info(f"🍽 Delivering {order.items[0]} to Table {order.table_number}" )
        self.state_machine.change_state(RobotState.DELIVER_FOOD)

        self.get_logger().info("🏠 Returning to Kitchen")
        self.state_machine.change_state(RobotState.RETURN_TO_KITCHEN)

    def order_callback(self, msg):
        self.get_logger().info(f"📥 Received: {msg.data}")

        parts = msg.data.split(",")

        order_id = int(parts[0])
        table_number = int(parts[1])
        items = [parts[2]]

        order = Order(order_id, table_number, items)
        self.process_order(order)
        self.serve_orders()
def main(args=None):
       rclpy.init(args=args)
       node = WaitRController()


       rclpy.spin(node)

       node.destroy_node()
       rclpy.shutdown()


if __name__ == "__main__":
    main()