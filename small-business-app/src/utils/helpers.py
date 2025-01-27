def validate_product_name(name):
    if not name or len(name) < 3:
        raise ValueError("Product name must be at least 3 characters long.")
    return name

def validate_product_price(price):
    if price < 0:
        raise ValueError("Product price cannot be negative.")
    return price

def validate_product_quantity(quantity):
    if quantity < 0:
        raise ValueError("Product quantity cannot be negative.")
    return quantity

def handle_error(error):
    print(f"Error: {error}")