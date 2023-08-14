#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        rows = len(matrix)
        if rows > 0 and len(matrix[0]) > 0:
            for i in range(rows):
                cols = len(matrix[i]) - 1
                for j in range(cols):
                    print("{:d}".format(matrix[i][j]), end=" ")
                print("{:d}".format(matrix[i][cols]))
        else:
            print()
