#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0 or n >= len(str):
        return str
    return str[:n] + str[n + 1:]


'''
def remove_char_at(str, n):
def: This defines a function.
remove_char_at: The name of the function.
str: The first parameter, a string.
n: The second parameter, the index of the character to remove.
:: Starts the function body.

if n < 0 or n >= len(str):
This checks if the index n is out of bounds:
n < 0: If n is negative, it's invalid.
or: Logical OR, meaning if either condition is true.
n >= len(str): If n is greater than or equal to the length of the string, it's also invalid.
len(str): Returns how many characters are in the string.

return str
If the index is invalid, just return the original string unchanged.

return str[:n] + str[n + 1:]
This is the main logic. It returns a new string made of two parts:
str[:n]
str[...]: Accessing part of the string using slicing.
:n: Means "from the beginning up to (but not including) index n".
Example: if str = "Holberton" and n = 3, str[:3] is "Hol".

str[n + 1:]
n + 1: We skip the character at index n.
str[n + 1:]: Means "from index n+1 to the end".
In the same example, str[4:] is "erton".

+
Joins the two parts: "Hol" + "erton" → "Holerton"
'''
