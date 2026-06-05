#!/usr/bin/python3


import json


class CustomObject:

    def __init__(self, name="John", age=23, is_student=True):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}\nAge: {self.age}\nIs Student: {self.is_student}")

    def serialize(self, filename):
        with open(filename, 'w', encoding="utf-8") as f:
            return json.dump(self.__dict__, f)

    @classmethod
    def deserialize(cls, filename):
        with open(filename, 'r', encoding="utf-8") as f:
            data = json.load(f)
            return cls(**data)
