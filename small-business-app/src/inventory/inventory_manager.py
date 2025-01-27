class InventoryManager:
    def __init__(self):
        self.inventory = []

    def add_product(self, name, quantity, price):
        product = {'name': name, 'quantity': quantity, 'price': price}
        self.inventory.append(product)

    def update_product(self, name, quantity, price):
        for product in self.inventory:
            if product['name'] == name:
                product['quantity'] = quantity
                product['price'] = price
                return True
        return False

    def delete_product(self, name):
        self.inventory = [product for product in self.inventory if product['name'] != name]

    def view_inventory(self):
        return self.inventory