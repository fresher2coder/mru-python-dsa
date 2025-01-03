class Product:
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock

    def update_stock(self, quantity):
        if quantity <= self.stock:
            self.stock -= quantity
            return True
        return False

    def get_details(self):
        return f"Product ID: {self.product_id}, Name: {self.name}, Price: {self.price}, Stock: {self.stock}"
