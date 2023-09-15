#!/usr/bin/python3
"""
This module is for class Base

"""


class Base:
    """
    base class 

    """
    __nb_objects = 0

    def __init__(self, id=None):
        """initial function
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
