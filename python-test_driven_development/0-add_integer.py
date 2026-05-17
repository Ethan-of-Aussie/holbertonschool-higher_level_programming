#!/usr/bin/python3
"""
Module provides function that sums two integers.
"""

def add_integer(a, b=98):
    """
    Function sums up two intergers
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
