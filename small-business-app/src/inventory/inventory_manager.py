class InventoryManager:
    def __init__(self):
        self.inventory = {}

    def add_product(self, product_id, product_name, quantity, price):
        if product_id in self.inventory:
            raise ValueError("Product ID already exists.")
        self.inventory[product_id] = {
            'name': product_name,
            'quantity': quantity,
            'price': price
        }

    def update_product(self, product_id, quantity=None, price=None):
        if product_id not in self.inventory:
            raise ValueError("Product ID does not exist.")
        if quantity is not None:
            self.inventory[product_id]['quantity'] = quantity
        if price is not None:
            self.inventory[product_id]['price'] = price

    def delete_product(self, product_id):
        if product_id not in self.inventory:
            raise ValueError("Product ID does not exist.")
        del self.inventory[product_id]

    def view_inventory(self):
        return self.inventory.copy()