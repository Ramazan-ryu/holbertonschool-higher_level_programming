#!/usr/bin/python3
"""A script that writes into a text file"""


def append_write(filename="", text=""):
    """A function that appends a string into a text file
    Arguments:
    filename:(string) the name of the file or its relative path
    text:(string) the string content to be written into the file
    Return: the number of characters written is returned
    """

    with open(filename, "a") as f:
        a = f.write(text)
        return a
