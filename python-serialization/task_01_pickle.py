#!/usr/bin/python3
# Defines class and serializes it

import pickle


class CustomObject:

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """method prints out attributes"""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """method serializes the current instance of the object"""
        try:
            with open(filename, "wb") as file:
                return pickle.dump(self, file)
        except Exception:
            return None
    
    @classmethod
    def deserialize(cls, filename):
        """method returns instance of custom object"""
        try:
            with open(filename, "rb") as file_rb:
                return pickle.load(file_rb)
        except Exception:
            return None
