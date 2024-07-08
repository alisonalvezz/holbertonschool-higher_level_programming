#!/usr/bin/python3
"""
Defines a Square
"""


class Square:
    """Defines a Square"""

    def __init__(self, size=0):
        """
        Initializes the square with a size
        Args:
            size(int): Size of the square (default is 0)
        """
        self.__size = size

    @property
    def size(self):
        """
        Returns:
            int: size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Args:
            value (int): size of the square
        Raises:
            TypeError: if value is not an integer
            ValueError: if value is negative
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates and returns the area of the square

        Returns:
            int: the area of the square (size ** 2)
        """
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for x in range(self.__size):
                print("#" * self.__size)
