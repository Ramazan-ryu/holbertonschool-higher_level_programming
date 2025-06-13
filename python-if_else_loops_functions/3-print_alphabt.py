#!/usr/bin/python3
print("".join("{}".format(chr(i)) for i in range(97, 123)
              if i != 101 and i != 113), end="")


# range(97, 123) — This creates a sequence of numbers from 97 to 122, which represent ASCII values for lowercase letters 'a' to 'z'.
# chr(i) — Converts each number i in the range to its corresponding ASCII character.
# if i != 101 and i != 113 — This condition skips the characters with ASCII codes 101 ('e') and 113 ('q').
# "{}".format(chr(i)) — Formats each character as a string (although this step is redundant here, just chr(i) would work).
# "".join(...) — Joins all the characters together into one single string without spaces.
# print(..., end="") — Prints the final string to the screen, without adding a newline at the end.
