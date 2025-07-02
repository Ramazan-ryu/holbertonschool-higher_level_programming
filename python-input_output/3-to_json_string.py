#!/usr/bin/python3
"""A script that returns the JSON representation of an object (string)"""
import json


def to_json_string(my_obj):
    """A function that serialises an object
    arguments:
    my_obj: the object to be serialised
    Return: A JSON string is returned
    """
    
    j = json.dump(my_obj)
    print(j)
