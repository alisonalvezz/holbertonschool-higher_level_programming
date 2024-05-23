#!/usr/bin/python3


class Square:
    """defines a Square
    Attributes:
        __size (int): size of the square
        area (int): area of the square
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        return self.__size ** 2
