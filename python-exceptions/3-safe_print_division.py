#!/usr/bin/python3
# Write a function that divides 2 integers and prints the result.
def safe_print_division(a, b):
    deleniye = None
    try:
        deleniye = a/b
    except ZeroDivisionError:
        pass
    finally:
        print("Inside result: {}".format(deleniye))
    return deleniye
