#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    max_v = my_list[0]
    for num in my_list:
        if num > max_v:
            max_v = num
    return max_v
