#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for li in matrix:
        for num in range(len(li)):
            print("{:d}".format(li[num]), end='')
            if num != len(li) - 1:
                print(' ', end='')
        print()
