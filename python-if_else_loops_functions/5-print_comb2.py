#!/usr/bin/python3
for i in range(100):
    print(("0" * (i < 10) + f"{i}"), end=", " * (i != 99) + "\n" * (i == 99))
