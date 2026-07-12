from order import Order


class OrderManager:
    def __init__(self):
        self.orders = []

    def add_order(self, order: Order):
        self.orders.append(order)
        print(f"✅ Order #{order.order_id} added.")

    def get_next_order(self):
        if len(self.orders) == 0:
            return None

        return self.orders.pop(0)

    def pending_orders(self):
        return len(self.orders)