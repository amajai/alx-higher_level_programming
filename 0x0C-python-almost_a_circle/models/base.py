#!/usr/bin/python3
"""
This module is for class Base

"""
import json
import os


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
        """returns the JSON string representation of list_dictionaries

        Args:
            list_dictionaries (list[dict,...]): list of dictionaries
        """
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        else:
            return "[]"

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string

        Args:
            from_json_string (str): string representing a list of dictionaries
        """
        if json_string:
            return json.loads(json_string)
        else:
            return []

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file

        Args:
            list_objs (list): list of instances who inherits from Base
        """
        path = "{}.json".format(cls.__name__)
        if list_objs:
            dict_list = [obj.to_dictionary() for obj in list_objs]
        else:
            dict_list = []
        with open(path, "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(dict_list))

    @classmethod
    def load_from_file(cls):
        """returns a list of instances
        """
        path = "{}.json".format(cls.__name__)
        if not os.path.exists(path):
            return []
        with open(path, "r", encoding="utf-8") as f:
            json_dict_list = f.read()
        dict_list = cls.from_json_string(json_dict_list)
        instance_list = []
        for obj in dict_list:
            instance = cls.create(**obj)
            instance_list.append(instance)
        return instance_list

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set

        Args:
            dictionary (dict): dictionary with key/value
        """
        if cls.__name__ == "Square":
            instance = cls(1)
        else:
            instance = cls(1, 1)
        instance.update(**dictionary)
        return instance
