#!/usr/bin/python3
"""
This module provides a function to format text by adding line breaks
after sentences ending with '.', '?', or ':'.

"""


def text_indentation(text):
    """prints a text with 2 new lines after each of these
    characters: '.', '?', or ':'.

    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    is_newline = False
    for c in text:
        if c not in ['.', '?', ':']:
            if c == " " and is_newline:
                print("", end="")
            else:
                print(c, end="")
                is_newline = False
        else:
            print(c, end="")
            print()
            print()
            is_newline = True
