#!/usr/bin/python3
"""Module defines MyList."""

class MyList(list):
    """Class MyList inherits a list."""


    def print_sorted(self):
        print(sorted(self))
