#!/usr/bin/python3
"""a class that is a subclass and initialises an object"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """a class Rectangle that inherits from BaseGeometry (7-base_geometry.py)
    Instantiation with width and height: def __init__(self, size)
    size  must be private. No getter or setter
    size  must be positive integers, validated by integer_validator"""
    def __init__(self, size):
