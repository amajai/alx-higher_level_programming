#!/usr/bin/python3
"""
This module is for class Base

"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string representation of list_dictionaries
        Args:
            list_dictionaries (list[dict,...]): list of dictionaries
        """
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        else:
            return "[]"
