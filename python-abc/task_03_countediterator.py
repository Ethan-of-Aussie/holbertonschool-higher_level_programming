#!/usr/bin/python3


class CountedIterator:

    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.__counter = 0

    def get_count(self):
        return self.__counter

    def __iter__(self):
        return self

    def __next__(self):
        value = next(self.iterator)
        self.__counter += 1
        return value
