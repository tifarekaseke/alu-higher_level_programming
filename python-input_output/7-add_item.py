#!/usr/bin/python3
"""Adds all arguments to a Python list, and then saves them to a file."""

import sys

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

    try:
        loadFile = load_from_json_file("add_item.json")
    except FileNotFoundError:
        loadFile = []

    # Iterate over command line arguments and append them to the list
    for idx in range(1, len(sys.argv)):
        loadFile.append(sys.argv[idx])

    # Save the updated list back to the file
    save_to_json_file(loadFile, "add_item.json")

