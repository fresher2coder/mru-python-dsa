from user import User
from product import Product
from cart import Cart
from order import Order

# Create users
user1 = User(user_id=1, name="Alice", email="alice@example.com")

# Create products
product1 = Product(product_id=101, name="Laptop", price=1000, stock=5)
product2 = Product(product_id=102, name="Smartphone", price=500, stock=10)

# View product details
print(product1.get_details())
print(product2.get_details())

# Create a cart and add items
cart = Cart()
cart.add_to_cart(product1, 2)  # Add 2 Laptops
cart.add_to_cart(product2, 3)  # Add 3 Smartphones
cart.view_cart()

# Remove an item from the cart
cart.remove_from_cart(product1.product_id)
cart.view_cart()

# Place an order
order = Order(user1, cart)
order.place_order()
