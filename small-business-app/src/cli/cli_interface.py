from importlib.resources import Package

def main():
    import sys
    from inventory.inventory_manager import InventoryManager

    inventory_manager = InventoryManager()

    while True:
        print("\nSmall Business Inventory Management")
        print("1. Add Product")
        print("2. Update Product")
        print("3. Delete Product")
        print("4. View Inventory")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter product name: ")
            quantity = int(input("Enter product quantity: "))
            price = float(input("Enter product price: "))
            inventory_manager.add_product(name, quantity, price)
            print(f"Product '{name}' added.")
        
        elif choice == '2':
            name = input("Enter product name to update: ")
            quantity = int(input("Enter new quantity: "))
            price = float(input("Enter new price: "))
            inventory_manager.update_product(name, quantity, price)
            print(f"Product '{name}' updated.")
        
        elif choice == '3':
            name = input("Enter product name to delete: ")
            inventory_manager.delete_product(name)
            print(f"Product '{name}' deleted.")
        
        elif choice == '4':
            inventory = inventory_manager.view_inventory()
            print("Current Inventory:")
            for product in inventory:
                print(product)
        
        elif choice == '5':
            print("Exiting the application.")
            sys.exit()
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()