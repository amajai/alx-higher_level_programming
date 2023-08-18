#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return [list(map(lambda n: n*n, arr)) for arr in matrix if matrix]
