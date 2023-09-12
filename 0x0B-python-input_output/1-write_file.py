#!/usr/bin/python3
"""
This module has a function (write_file) where it writes string
to text file and return number of characters

"""


def write_file(filename="", text=""):
    """string to a text file (UTF8) and returns the number
    of characters written
    """
    with open(filename, "w+", encoding="utf-8") as f:
        f.write(text)
        return f.tell()
