#!/usr/bin/python3
# Write a function that divides element by element 2 lists
def list_division(my_list_1, my_list_2, list_length):
    res = []
    for n in range(list_length):
        itoq = 0
        try:
            itoq = my_list_1[n]/my_list_2[n]
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            res.append(itoq)
    return res
