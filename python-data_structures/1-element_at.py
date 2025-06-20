#!/usr/bin/python3
def element_at(my_list, idx):
    idx=int(input("write:"))
    for idx in my_list:
        if idx>0 and idx<4:
            print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))
        else:
            print("None")
