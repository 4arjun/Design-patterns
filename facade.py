class Inventory:
    def check_stock(self, product):
        print(f"Checking stock for {product}")


class Payment:
    def process_payment(self, amount):
        print(f"Processing payment of ₹{amount}")


class Order:
    def create_order(self, product):
        print(f"Creating order for {product}")


class Notification:
    def send_confirmation(self):
        print("Sending confirmation")


class OrderFacade:

    def __init__(self):
        self.inventory = Inventory()
        self.payment = Payment()
        self.order = Order()
        self.notification = Notification()

    def place_order(self, product, amount):
        self.inventory.check_stock(product)
        self.payment.process_payment(amount)
        self.order.create_order(product)
        self.notification.send_confirmation()


facade = OrderFacade()

facade.place_order("iPhone", 80000)



# without

# inventory.check_stock()
# payment.process_payment()
# order.create_order()
# notification.send_confirmation()