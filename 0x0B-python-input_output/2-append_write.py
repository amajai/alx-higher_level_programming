#!/usr/bin/python3
"""
This module has a function (append_write) that appends a string at the
end of a text file and returns the number 

"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file (UTF8) and returns
    the number of characters added
    """
    with open(filename, "a+", encoding="utf-8") as f:
        f.write(text)
        return len(text)
