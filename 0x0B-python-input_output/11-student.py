#!/usr/bin/python3
"""
This module has class (Student) with attributes

"""


class Student:
    """
    Class containing attributes of a student
    first_name, last_name and age

    """
    def __init__(self, first_name, last_name, age):
        """Student instance attributes
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance
        """
        if attrs is None:
            return self.__dict__
        dict = {}
        for k in attrs:
            v = self.__dict__.get(k)
            if v:
                dict[k] = v
        return dict

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance:
        """
        self.first_name = json["first_name"]
        self.last_name = json["last_name"]
        self.age = json["age"]
