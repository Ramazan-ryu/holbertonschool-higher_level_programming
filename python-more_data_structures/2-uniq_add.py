#!/usr/bin/python3
def uniq_add(my_list=[]):
    total = 0
    new_list = []
    for x in my_list:
        if x not in new_list:
            new_list.append(x)
            total += x
    return total
