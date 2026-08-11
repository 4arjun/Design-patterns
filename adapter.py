class PaymentProcessor:

    def pay(self, amount):
        pass


class Stripe:

    def make_payment(self, amount):
        print(f"Stripe payment: ₹{amount}")


class StripeAdapter(PaymentProcessor):

    def __init__(self):
        self.stripe = Stripe()

    def pay(self, amount):
        self.stripe.make_payment(amount)

processor = StripeAdapter()

processor.pay(5000)