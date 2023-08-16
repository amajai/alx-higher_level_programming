#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix and len(matrix) > 0:
        new_matrix = []
        for arr in matrix:
            new_matrix.append(list(map(lambda n: n*n, arr)))
        return new_matrix
    return matrix
