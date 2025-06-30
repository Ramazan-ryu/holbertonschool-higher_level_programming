#!/usr/bin/python3
"""creates a class that raises an exception"""


class BaseGeometry:
    """this class raises an exception"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        elif value < 0 or value == 0:
            raise ValueError(f"{name} must be greater than 0.")
