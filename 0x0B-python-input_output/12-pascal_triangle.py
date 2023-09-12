#!/usr/bin/python3
"""
This module has function (pascal_triangle) returns a list of lists of
integers representing the Pascal's triangle of n

"""


def pascal_triangle(n):
    """Returns a list of lists of integers representing the Pascal's
    triangle of n
    """
    if n <= 0:
        return []
    result = []
    base_list = [1]
    old_list = []
    for i in range(1, n+1):
        curr_list = base_list * i
        if i >= 3:
            for j in range(1, len(curr_list) - 1):
                curr_list[j] = old_list[j-1] + old_list[j]
        old_list = curr_list
        result.append(curr_list)
    return result
