# Small Business Application

This is a small business application designed to manage inventory efficiently. It provides a command-line interface for users to interact with the inventory system, allowing them to add, update, delete, and view products.

## Project Structure

```
small-business-app
├── src
│   ├── __init__.py
│   ├── main.py
│   ├── inventory
│   │   ├── __init__.py
│   │   └── inventory_manager.py
│   ├── cli
│   │   ├── __init__.py
│   │   └── cli_interface.py
│   └── utils
│       ├── __init__.py
│       └── helpers.py
├── requirements.txt
├── setup.py
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd small-business-app
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the application, execute the following command:
```
python src/main.py
```

Follow the on-screen instructions to manage your inventory.

## Features

- Add new products to the inventory
- Update existing product details
- Delete products from the inventory
- View the current inventory status

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License.