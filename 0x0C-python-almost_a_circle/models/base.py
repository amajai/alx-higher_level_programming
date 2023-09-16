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

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file

        Args:
            list_objs (list): list of instances who inherits from Base
        """
        path = "{}.json".format(cls.__name__)
        dict_list = [obj.to_dictionary() for obj in list_objs]
        with open(path, "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(dict_list))
