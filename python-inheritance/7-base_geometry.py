#!/usr/bin/python3
"""creates a class that raises an exception"""


class BaseGeometry:
    """this class raises an exception"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        elif value < 0 or value == 0:
            raise ValueError("{} must be greater than 0.".format(name))
