#!/usr/bin/python3
"""
Geometry module defining Shape, Circle, Rectangle, and a helper function
for displaying shape information.
"""


from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """Abstract base class for geometric shapes."""

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    """Represents a circle with a given radius."""

    def __init__(self, radius):
        self.radius = radius

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, value):
        self.__radius = value

    def area(self):
        return pi * (self.__radius * self.__radius)

    def perimeter(self):
        return 2 * (pi * self.__radius)

class Rectangle(Shape):
    """Represents a rectangle defined by width and height."""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * (self.__width + self.__height)

def shape_info(Shape):
    """Prints the area and perimeter of a Shape instance."""
    print("Area:", Shape.area())
    print("Perimeter:", Shape.perimeter())
