#!/usr/bin/python3
"""Module defines both serialize_and_save_to_file, load_and_deserialize."""

import json


def serialize_and_save_to_file(data, filename):
    """Save a Python object to a file as JSON."""
    with open(filename, "w", encoding="utf-8") as f:
        return json.dump(data, f)

def load_and_deserialize(filename):
    """Load JSON data from a file into a Python object."""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
