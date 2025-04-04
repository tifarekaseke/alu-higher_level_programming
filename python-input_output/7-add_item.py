#!/usr/bin/python3
import sys
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

def main():
    # Define the file path for the JSON file
    file_path = "add_item.json"

    # Attempt to load the current list from the file if it exists
    try:
        items = load_from_json_file(file_path)
    except FileNotFoundError:
        # If file doesn't exist, initialize an empty list
        items = []

    # Add all command-line arguments (excluding the script name) to the list
    items.extend(sys.argv[1:])

    # Save the updated list back to the JSON file
    save_to_json_file(items, file_path)

if __name__ == "__main__":
    main()


