#!/usr/bin/python3
"""A Square Module

"""


class Square:
    """A Square class

    """
    def __init__(self, size=0):
        """Initialize instances of Square

        Args:
          size (int): Define size of square. 0 is the default value.

        """
        self.size = size

    @property
    def size(self):
        """Get size of Square.

        Returns:
            Private size of Square

        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set size of Square.

        Args:
            value (int): Size of Square

        """
        self.__size = value
        if type(self.__size) is not int:
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Get area of a Square.

        Returns:
            size * size

        """
        return self.__size * self.__size
