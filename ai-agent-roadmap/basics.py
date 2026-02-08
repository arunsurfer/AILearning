"""
Grocery List App - function + dict + JSON + error-handling examples

This version demonstrates:
- functions (`process_text`, `parse_json_response`, CRUD helpers)
- dict usage to store item -> quantity
- for loops for iteration
- basic error handling (try/except, validation)
- a non-interactive `demo` mode for quick verification
"""

import json
import sys
from typing import Dict, Any, Optional


def process_text(text: str) -> Dict[str, Any]:
    """Simple text-processing helper.

    Returns a dict with normalized text, words and word count.
    """
    normalized = text.strip()
    words = normalized.split()
    return {
        "original": text,
        "normalized": normalized.lower(),
        "word_count": len(words),
        "words": words,
    }


def parse_json_response(json_str: str) -> Optional[Dict[str, Any]]:
    """Safely parse a JSON string into a Python dict.

    Returns None on parse error and prints the error message.
    """
    try:
        return json.loads(json_str)
    except json.JSONDecodeError as exc:
        print("Failed to parse JSON:", exc)
        return None


def add_item(grocery: Dict[str, int], item: str, quantity: str) -> None:
    try:
        qty = int(quantity)
    except ValueError:
        raise ValueError("Quantity must be an integer")
    grocery[item] = grocery.get(item, 0) + qty


def remove_item(grocery: Dict[str, int], item: str) -> bool:
    if item in grocery:
        del grocery[item]
        return True
    return False


def update_quantity(grocery: Dict[str, int], item: str, quantity: str) -> bool:
    if item not in grocery:
        return False
    try:
        qty = int(quantity)
    except ValueError:
        raise ValueError("Quantity must be an integer")
    grocery[item] = qty
    return True


def view_list(grocery: Dict[str, int]) -> None:
    if not grocery:
        print("List is empty!")
        return
    print("\nGrocery List:")
    for item, qty in grocery.items():
        print(f"- {item}: {qty}")


def run_demo() -> None:
    """Run a non-interactive demo showcasing the helpers."""
    print("Running demo...")
    grocery: Dict[str, int] = {}

    print("\n1) Demonstrate `process_text()`")
    txt = "  Apples and oranges  "
    result = process_text(txt)
    print(result)

    print("\n2) Demonstrate `parse_json_response()`")
    good = '{"item": "banana", "qty": 3}'
    bad = '{item: banana, qty:}'
    print("Good JSON ->", parse_json_response(good))
    print("Bad JSON ->", parse_json_response(bad))

    print("\n3) Demonstrate add/update/remove with validation")
    try:
        add_item(grocery, "apple", "2")
        add_item(grocery, "banana", "3")
        print("After adds:")
        view_list(grocery)
        update_quantity(grocery, "apple", "5")
        print("After update:")
        view_list(grocery)
        removed = remove_item(grocery, "banana")
        print("Removed banana?", removed)
        view_list(grocery)
    except ValueError as e:
        print("Validation error during demo:", e)


def main_menu() -> None:
    grocery: Dict[str, int] = {}
    while True:
        print("\nOptions:")
        print("1. Add item")
        print("2. View list")
        print("3. Remove item")
        print("4. Update quantity")
        print("5. Process text input (example)")
        print("6. Parse JSON input (example)")
        print("7. Exit")
        choice = input("Choose an option: ")

        match choice:
            case '1':
                item = input("Enter the item to add: ")
                quantity = input("Enter quantity: ")
                try:
                    add_item(grocery, item, quantity)
                    print(f"{item} (qty: {grocery[item]}) added/updated.")
                except ValueError as e:
                    print("Error:", e)

            case '2':
                view_list(grocery)

            case '3':
                item = input("Enter the item to remove: ")
                if remove_item(grocery, item):
                    print(f"{item} removed from the list.")
                else:
                    print(f"{item} not found in the list.")

            case '4':
                item = input("Enter the item to update: ")
                quantity = input("Enter new quantity: ")
                try:
                    if update_quantity(grocery, item, quantity):
                        print(f"{item} quantity updated to {grocery[item]}.")
                    else:
                        print(f"{item} not found in the list.")
                except ValueError as e:
                    print("Error:", e)

            case '5':
                text = input("Enter some text to process: ")
                print(process_text(text))

            case '6':
                js = input("Enter a JSON string to parse: ")
                parsed = parse_json_response(js)
                print("Parsed:", parsed)

            case '7':
                print("Exiting the app. Goodbye!")
                break

            case _:
                print("Invalid option. Please try again.")


if __name__ == "__main__":
    # Allow running a quick non-interactive demo: `python basics.py demo`
    if len(sys.argv) > 1 and sys.argv[1] == "demo":
        run_demo()
    else:
        main_menu()

