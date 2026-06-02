#!/usr/bin/python3
"""This file uses the Modules to create a new file and add to the file."""


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

import sys


filename = "add_item.json"
try:
    my_list = load_from_json_file(filename)
except FileNotFoundError:
    my_list = []

save_to_json_file(my_list + sys.argv[1:], filename)
