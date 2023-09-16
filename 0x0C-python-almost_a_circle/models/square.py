#!/usr/bin/python3
"""
This module is for a class representing Square

"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    A Square class

    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initial instance of Square

        Args:
            size (int): Define size of square.
            x (int or optional): x value. Default is 0
            y (int or optional): y value. Default is 0
            id (int or None): id value. Default is None
        """
        super().__init__(id=id, width=size, height=size, x=x, y=y)
        self.x = x
        self.y = y
        self.size = size

    def __str__(self):
        xy = "{:d}/{:d}".format(self.x, self.y)
        return f"[Square] ({self.id}) {xy} - {self.width}"
