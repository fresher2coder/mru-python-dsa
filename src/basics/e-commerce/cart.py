class Cart:
    def __init__(self):
        self.items = {}

    def add_to_cart(self, product, quantity):
        if product.update_stock(quantity):
            if product.product_id in self.items:
                self.items[product.product_id]['quantity'] += quantity
            else:
                self.items[product.product_id] = {'product': product, 'quantity': quantity}
            print(f"Added {quantity} {product.name}(s) to cart.")
        else:
            print(f"Sorry, {product.name} is out of stock.")

    def remove_from_cart(self, product_id):
        if product_id in self.items:
            removed_item = self.items.pop(product_id)
            print(f"Removed {removed_item['product'].name} from cart.")
        else:
            print("Product not in cart.")

    def view_cart(self):
        print("Cart Items:")
        for item in self.items.values():
            product = item['product']
            print(f"{product.name}: {item['quantity']} @ {product.price} each")
