#!/usr/bin/python3
# Write a function that prints x elements of a list.
def safe_print_list(my_list=[], x=0):
    count = 0
    for z in range(x):
        try:
            print(my_list[z], end=" ")
            count += 1
        except IndexError:
            break
        print(end="")
    return count
