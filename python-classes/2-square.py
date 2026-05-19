#!/usr/bin/python3
""" Module defines class Square"""

class Square:
    """ class Square defines size of square"""

    def __init__(self, size=0):
        """ Initialize's size of class Square"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
