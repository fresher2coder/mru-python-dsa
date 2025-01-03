class Order:
    def __init__(self, user, cart):
        self.user = user
        self.cart = cart
        self.order_total = 0

    def place_order(self):
        if not self.cart.items:
            print("Cart is empty. Add items to place an order.")
            return
        self.order_total = sum(
            item['product'].price * item['quantity'] for item in self.cart.items.values()
        )
        print(f"Order placed successfully for {self.user.name}.")
        print(f"Total amount: {self.order_total}")
        print("Order Details:")
        self.cart.view_cart()
        self.cart.items = {}  # Clear the cart after placing the order
