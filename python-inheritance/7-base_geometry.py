#!/usr/bin/python3
"""Module defines class BaseGeometry."""


class BaseGeometry:
    """Validates value, area not finished."""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        if isinstance(name, tuple) or isinstance(value, tuple):
            raise TypeError("'name' and 'value' must not be a tuple")
        if isinstance(name, list) or isinstance(value, list):
            raise TypeError("'name' and 'value' must not be a list")
        if isinstance(name, dict) or isinstance(value, dict):
            raise TypeError("'name' and 'value' must not be a dictionary")
        if value is None:
            raise ValueError("must not be None")
        if isinstance(value, bool):
            raise ValueError("'value' must not be a boolen")
