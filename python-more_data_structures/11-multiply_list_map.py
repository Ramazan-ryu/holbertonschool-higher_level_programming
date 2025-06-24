#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    return(list(map(lambda x: x * number, my_list)))
'''list — converts an iterator (e.g. result map) into a list.

lambda is a small function without a name, such as lambda x: x * number.

return — returns a value from a function.

map — applies a function ( lambda) to each element of a list and returns an iterator with the results.

Concatenation:
return list(map(lambda x: x * number, my_list))'''
