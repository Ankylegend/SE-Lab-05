"""
A simple inventory management system.

This module allows adding, removing, and querying items in an inventory,
as well as loading from and saving to a JSON file.
"""

import json
from datetime import datetime


def add_item(stock, item="default", qty=0, logs=None):
    """Add a specified quantity of an item to the stock."""
    if logs is None:
        logs = []

    if not isinstance(qty, (int, float)):
        print(f"Error: Quantity '{qty}' for item '{item}' is not valid.")
        print("Skipping item.")
        return

    if not item:
        return
    stock[item] = stock.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")


def remove_item(stock, item, qty):
    """Remove a specified quantity of an item from the stock."""
    try:
        stock[item] -= qty
        if stock[item] <= 0:
            del stock[item]
    except KeyError:
        print(f"Error removing item: '{item}' not found in stock")


def get_qty(stock, item):
    """Get the current quantity of a specific item."""
    return stock[item]


def load_data(file="inventory.json"):
    """Load inventory data from a JSON file and return it."""
    try:
        with open(file, "r", encoding="utf-8") as f:
            return json.loads(f.read())
    except FileNotFoundError:
        print(f"Warning: {file} not found. Starting with an empty inventory.")
        return {}
    except json.JSONDecodeError:
        print(f"Error: Could not decode {file}.")
        print("Starting with an empty inventory.")
        return {}


def save_data(data_to_save, file="inventory.json"):
    """Save the provided inventory data to a JSON file."""
    with open(file, "w", encoding="utf-8") as f:
        f.write(json.dumps(data_to_save))


def print_data(stock):
    """Print a report of all items in stock."""
    print("Items Report")
    for item, qty in stock.items():
        print(f"{item} -> {qty}")


def check_low_items(stock, threshold=5):
    """Return a list of items with stock below the threshold."""
    result = []
    for item, qty in stock.items():
        if qty < threshold:
            result.append(item)
    return result


def main():
    """Main function to run the inventory operations."""
    stock = load_data()  # Initialize local stock from file

    add_item(stock, "apple", 10)
    add_item(stock, "banana", -2)
    add_item(stock, 123, "ten")
    remove_item(stock, "apple", 3)
    remove_item(stock, "orange", 1)

    try:
        print("Apple stock:", get_qty(stock, "apple"))
    except KeyError:
        print("Apple stock: 0")

    print("Low items:", check_low_items(stock))
    save_data(stock)
    print_data(stock)


if __name__ == "__main__":
    main()
