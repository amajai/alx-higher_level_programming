#!/usr/bin/python3
"""
A module provides a function to print a person's name based on their
first and last names.

"""


def say_my_name(first_name="", last_name=""):
    """Print a person's name based on their first and last names.

    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
