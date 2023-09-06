#!/usr/bin/python3
matrix_divided = __import__('2-matrix_divided').matrix_divided

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
matrix2 = [
    [1, 2, 3],
    [4, 5, 6, 5],
    [4, 5, 6]
]
matrix3 = [
    [1, 2, 3],
    [2, "hello", 5],
    [4, 5, 6]
]
matrix4 = [2, 4, 5]
matrix5 = [
    [4, 5, 6]
]
matrix6 = [
    [],
    [],
    []
]
matrix7 = [
    [1, 2, 3],
    [4, 5, 9],
    [4, 5, 5, 5]
]
print(matrix_divided(matrix, 3))
try:
    print(matrix_divided(matrix2, 3))
except Exception as e:
    print(e)
try:
    print(matrix_divided(matrix3, 3))
except Exception as e:
    print("matrix 3:", e)

try:
    print(matrix_divided(matrix4, 3))
except Exception as e:
    print("matrix 4:", e)
print(matrix_divided(matrix5, 3))
try:
    print(matrix_divided(matrix6, 2))
except Exception as e:
    print("matrix 6:", e)
try:
    print(matrix_divided(matrix7, 0.7))
except Exception as e:
    print("matrix 7:", e)

print(matrix)