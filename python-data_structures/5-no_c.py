#!/usr/bin/python3
def no_c(my_string):
    i = 0
    result = ""
    while i < len(my_string):
        char = my_string[i]
        if char != "C" and char !="c":
            result += char
        i += 1
    return result
