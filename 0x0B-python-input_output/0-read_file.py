#!/usr/bin/python3
"""
This module has function read_file that read text file
and print it out

"""


def read_file(filename=""):
    """function that reads a text file (UTF8) and
    prints it to stdout
    """

    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line, end="")
