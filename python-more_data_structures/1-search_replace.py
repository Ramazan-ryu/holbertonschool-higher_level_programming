#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_my_list = []
    for x in my_list:
        if x == search:
            new_my_list.append(replace)
        else:
            new_my_list.append(x)            
    return new_my_list

