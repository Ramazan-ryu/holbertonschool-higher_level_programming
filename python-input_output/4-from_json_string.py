#!/usr/bin/python3
"""A script that converts a string to JSON object"""
import json


def from_json_string(my_str):
    """Function that creates deserialises a string"""
    j = json.loads(my_str)
    return j
