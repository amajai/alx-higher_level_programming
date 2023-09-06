#!/usr/bin/python3
import doctest
"""
This module provides a function to print a square of
a specified size.

"""


def print_square(size):
    """Print a square of a specified size using hash symbols.

    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float):
        raise TypeError("size must be an integer")
    for _ in range(size):
        print("#"*size)
