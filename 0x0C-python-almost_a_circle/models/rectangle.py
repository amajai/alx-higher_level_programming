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

    def area(self):
        """Get area of a Rectangle.

        Returns:
            the current rectangle area - width * height
        """
        return self.__width * self.__height

    def display(self):
        """ prints in stdout the Rectangle instance with the character #
        """
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def update(self, *args, **kwargs):
        """ assigns new argument value to each attribute

        Args:
            args (list): list of arguments
            kwargs (dict): dictionary with key/value
        """
        if args:
            if len(args) > 0:
                super().__init__(args[0])
            if len(args) > 1:
                self.__width = args[1]
            if len(args) > 2:
                self.__height = args[2]
            if len(args) > 3:
                self.__x = args[3]
            if len(args) > 4:
                self.__y = args[4]

        if kwargs:
            if kwargs.get("id"):
                super().__init__(kwargs.get("id"))
            if kwargs.get("width"):
                self.__width = kwargs.get("width")
            if kwargs.get("height"):
                self.__height = kwargs.get("height")
            if kwargs.get("x"):
                self.__x = kwargs.get("x")
            if kwargs.get("y"):
                self.__y = kwargs.get("y")

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle
        """
        return {
            "x": self.x,
            "y": self.y,
            "id": self.id,
            "height": self.height,
            "width": self.width
        }

    def __str__(self):
        """returns string representation of class object
        """
        wh = "{:d}/{:d}".format(self.width, self.height)
        xy = "{:d}/{:d}".format(self.x, self.y)
        return f"[Rectangle] ({self.id}) {xy} - {wh}"
