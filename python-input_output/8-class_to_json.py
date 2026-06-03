#!/usr/bin/python3
"""Module defines class_to_json."""


def class_to_json(obj):
    """JSON serialization of an object."""
    return obj.__dict__
