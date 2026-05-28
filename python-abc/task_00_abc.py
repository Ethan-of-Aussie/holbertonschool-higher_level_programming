#!/usr/bin/python3
"""Define an abstract Animal class and
subclasses that implement sound behavior."""


from abc import ABC, abstractmethod


class Animal(ABC):
    """Represent an abstract animal
    that requires subclasses to define a sound."""

    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    """Represent a dog that produces a barking sound."""

    def sound(self):
        return "Bark"

class Cat(Animal):
    """Represent a cat that produces a meowing sound."""

    def sound(self):
        return "Meow"
