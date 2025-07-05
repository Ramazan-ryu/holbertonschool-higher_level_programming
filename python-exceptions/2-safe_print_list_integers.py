#!/usr/bin/python3
# Write a function that prints
# the first x elements of a list and only integers.
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for c in range(x):
        try:
            print("{:d}".format(my_list[c]), end="")
            count += 1
        except (TypeError, ValueError):
            pass
        except IndexError:
            break
    print()
    return count
