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

    def to_json(self):
        """Retrieves a dictionary representation of a Student instance
        """
        return self.__dict__
