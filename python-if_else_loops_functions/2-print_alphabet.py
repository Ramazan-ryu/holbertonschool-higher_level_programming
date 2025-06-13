#!/usr/bin/python3
print("".join("{}".format(chr(i)) for i in range(97, 123)), end="")
#range(97, 123) — range of ASCII codes for lowercase English letters (a–z).
#chr(i) — converts ASCII code to character.
#"{}".format(...) — formats each character as specified.
#"".join(...) — concatenates all characters into one string.
#end="" in print() — to avoid adding a line break at the en
