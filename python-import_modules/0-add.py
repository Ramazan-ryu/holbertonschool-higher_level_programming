#!/usr/bin/python3

from add_0 import add
#Imports the add function from the file add_0.py
if __name__ == "__main__":
#Runs the code block only if the script is executed directly    
    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))
