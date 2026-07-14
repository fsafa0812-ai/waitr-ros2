import rclpy
import time
from rclpy.node import Node

from .order import Order
from .restaurant_map import TABLES
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
    def get_preparation_time(self, item):
        # Simulate preparation time based on the item
        prep_times = {
            "Pizza": 5,
            "Burger": 3,
            "Sushi": 7,
            "Pasta": 4,
            "Coffee": 2,
        }
        return prep_times.get(item, 5)  # Default to 5 seconds if item not found
    
    def serve_orders(self):
      while self.order_manager.pending_orders() > 0:

        order = self.order_manager.get_next_order()

        self.get_logger().info(
            f"🚀 Serving Order #{order.order_id}"
        )

        self.get_logger().info("🏠 Going to Kitchen")
        self.state_machine.change_state(RobotState.GO_TO_KITCHEN)

        item = order.items[0]
        prep_time = self.get_preparation_time(item)
        
        self.get_logger().info(
        f"🍳 Preparing {item} for {prep_time} seconds"
        )

        time.sleep(prep_time)

        self.state_machine.change_state(RobotState.PICK_FOOD)

        destination = TABLES.get(order.table_number)

        print("DEBUG TABLE NUMBER:", order.table_number)
        print("DEBUG DESTINATION:", destination)

        self.get_logger().info(
        f"🧭 Navigating to Table {order.table_number}"
        )

        self.get_logger().info(
        f"📍 Destination Coordinates: {destination}"
        )
        self.state_machine.change_state(RobotState.GO_TO_TABLE)

        self.get_logger().info(
            f"🍽 Delivering {order.items[0]} to Table {order.table_number}"
        )
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