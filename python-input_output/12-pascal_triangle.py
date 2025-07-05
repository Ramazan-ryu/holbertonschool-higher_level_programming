#!/usr/bin/python3
'''Technical interview preparation'''


def pascal_triangle(n):
    '''Create a function def pascal_triangle(n): that returns a list of lists
    of integers representing the Pascal's triangle of n
    Returns an empty list if n <= 0
    You can assume n will be always an integer
    You are not allowed to import any module'''
    triangle = []
    for i in range(n):
        if i == 0:
            row = [1]
        else:
            prev_row = triangle[-1]
            row = [1]
            for j in range(1, len(prev_row)):
                row.append(prev_row[j - 1] + prev_row[j])
            row.append(1)
        triangle.append(row)
    return triangle
