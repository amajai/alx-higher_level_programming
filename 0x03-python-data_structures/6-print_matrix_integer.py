#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        rows = len(matrix)
        if rows > 0:
            for i in range(rows):
                for j in range(len(matrix[i])):
                    print("{}".format(matrix[i][j]), end=" ")
                print()
