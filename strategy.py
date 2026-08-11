# problem


# class Payment:
#     def pay(self, method, amount):

#         if method == "card":
#             print(f"Paying ₹{amount} using Card")

#         elif method == "upi":
#             print(f"Paying ₹{amount} using UPI")

#         elif method == "paypal":
#             print(f"Paying ₹{amount} using PayPal")

class PaymentStrategy:
    def pay(self, amount):
        pass

class CardPayment(PaymentStrategy):

    def pay(self, amount):
        print(f"Paying ₹{amount} using Card")

class UPIPayment(PaymentStrategy):

    def pay(self, amount):
        print(f"Paying ₹{amount} using UPI")

class Payment:

    def __init__(self, strategy):
        self.strategy = strategy

    def pay(self, amount):
        self.strategy.pay(amount)

payment = Payment(CardPayment())

payment.pay(1000)