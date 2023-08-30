#!/usr/bin/python3
"""A Square Module

"""


class Square:
    """A Square class

    """
    def __init__(self, size=0, position=(0, 0)):
        """Initialize instances of Square

        Args:
          size (int): Define size of square. 0 is the default value.
          position (int, int): tuple of 2 positive integers

        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Get position of Square.

        Returns:
            Private position of Square

        """
        return self.__position

    @position.setter
    def position(self, value):
        """Set position of Square.

        Args:
            value (int): Position of Square

        """
        self.__position = value
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if self.__position[0] < 0 or self.__position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """Get area of a Square.

        Returns:
            the current square area - size * size

        """
        return self.__size * self.__size

    def my_print(self):
        """prints in stdout the square with the character #
        with position spaces


        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.size):
                print(" " * self.__position[0], end="")
                for _ in range(self.size):
                    print('#', end="")
                print()
