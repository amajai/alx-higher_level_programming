#!/usr/bin/python3
"""
A module that provides 'add_integer()' that adds two integers or floats.
Takes two arguments, `a` and `b`, and returns their sum as an integer

"""


def add_integer(a, b=98):
    """Add two integers or floats and return the result as an integer.
    Return: The sum of 'a' and 'b' as an integer.
    """

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
