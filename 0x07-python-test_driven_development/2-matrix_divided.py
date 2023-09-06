#!/usr/bin/python3
"""
A module that provides 'matrix_divided()' for dividing each element in
a matrix by a given divisor.

"""


def matrix_divided(matrix, div):
    """Divide each element in a matrix by a given divisor.
    Return: a new matrix with divided values.
    """
    list_err = "matrix must be a matrix (list of lists) of integers/floats"
    size_err = "Each row of the matrix must have the same size"
    if type(matrix) is not list:
        raise TypeError(list_err)
    if len(matrix) == 0:
        raise TypeError(list_err)
    if type(matrix[0]) is not list:
        raise TypeError(list_err)
    matrix_limit = len(matrix[0])
    for i in range(len(matrix)):
        if type(matrix[i]) is not list:
            raise TypeError(list_err)
        if len(matrix[i]) == 0:
            raise TypeError(list_err)
        for j in range(len(matrix[i])):
            if type(matrix[i][j]) not in [int, float]:
                raise TypeError(list_err)
        if len(matrix[i]) != matrix_limit:
            raise TypeError(size_err)

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []

    for i in range(len(matrix)):
        new_matrix.append([])
        for j in range(len(matrix[i])):
            n = matrix[i][j]
            n = n / div
            new_matrix[i].append(round(n, 2))
    return new_matrix
