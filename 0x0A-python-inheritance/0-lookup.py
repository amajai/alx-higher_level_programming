#!/usr/bin/python3
"""
A module that provides function that returns the list of available
python attributes and methods

"""


def lookup(obj):
    """function that returns the list of available attributes
    and methods of an object
    """
    return dir(obj)
