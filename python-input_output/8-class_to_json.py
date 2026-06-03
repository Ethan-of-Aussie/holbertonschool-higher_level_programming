#!/usr/bin/python3
"""Module defines class_to_json."""

import json


def class_to_json(obj):
    """JSON serialization of an object."""
    return json.dumps(obj.__dict__)
