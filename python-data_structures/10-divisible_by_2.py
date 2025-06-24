#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    result = []
    i = 0
    while i < len(my_list):
        result.append(my_list[i] % 2 == 0)
        i += 1
    return result
