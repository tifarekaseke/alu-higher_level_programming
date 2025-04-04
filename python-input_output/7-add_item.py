#!/usr/bin/python3
import sys
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

def main():
    # Initialize the file path
    file_path = "add_item.json"

    # Try to load the existing list from the JSON file
    try:
        items = load_from_json_file(file_path)
    except FileNotFoundError:
        items = []

    # Add the arguments (excluding the script name)
    items.extend(sys.argv[1:])

    # Save the updated list to the JSON file
    save_to_json_file(items, file_path)

if __name__ == "__main__":
    main()

