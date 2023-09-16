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
        self.x = x
        self.y = y
        super().__init__(id=id, width=size, height=size, x=x, y=y)

    @property
    def size(self):
        """Get size of Square.

        Returns:
            size of Square
        """
        return self.width

    @size.setter
    def size(self, value):
        """Get size of Square.

        Args:
           value (int): Size of size
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ assigns new argument value to each attribute

        Args:
            args (list): list of arguments
            kwargs (dict): dictionary with key/value
        """
        _size = self.size
        if args:
            if len(args) > 0:
                super().__init__(id=args[0], width=_size, height=_size)
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            if kwargs:
                if kwargs.get("id"):
                    _id = kwargs.get("id")
                    _x = self.x
                    _y = self.y
                    super().__init__(_size, _size, _x, _y, _id)
                if kwargs.get("size"):
                    self.size = kwargs.get("size")
                if kwargs.get("x"):
                    self.x = kwargs.get("x")
                if kwargs.get("y"):
                    self.y = kwargs.get("y")

    def __str__(self):
        """returns string representation of class object
        """
        xy = "{:d}/{:d}".format(self.x, self.y)
        return f"[Square] ({self.id}) {xy} - {self.width}"
