#!/usr/bin/python3
"""a script that creates a class"""


class Student:
    """a class called student that has the following atttributes
        Attributes:
            first_name
            last_name
            age
            _json: retrieves a dictionary of the instance attributes
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if isinstance(attrs, list):
            slov = {}
            for name in attrs:
                if hasattr(self, name):
                    slov[name] = getattr(self, name)
            return slov
        else:
            return self.__dict__
