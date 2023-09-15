#!/usr/bin/python3
"""
This module is for a class representing Rectangle

"""
from models.base import Base


class Rectangle(Base):
    """
    A Rectangle class

    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initial instance of Rectangle

        Args:
            width (int): width of rectangle
            height (int): height of rectangle
            x (int or optional): x value. Default is 0
            y (int or optional): y value. Default is 0
            id (int or None): id value. Default is None
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Get width of Rectangle.

        Returns:
            Private width of Rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Get width of Rectangle.

        Args:
           value (int): Size of width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get height of Rectangle.

        Returns:
            Private height of Rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Get height of Rectangle.

        Args:
           value (int): Size of height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get x of Rectangle.

        Returns:
            Private x of Rectangle
        """
        return self.__x

    @x.setter
    def x(self, value):
        """Get x of Rectangle.

        Args:
           value (int): Value of x
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get y of Rectangle.

        Returns:
            Private y of Rectangle
        """
        return self.__y

    @y.setter
    def y(self, value):
        """Get y of Rectangle.

        Args:
           value (int): Value of y
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
