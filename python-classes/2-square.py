#!/usr/bin/python3


class Square:
    """Define a class square
    """
    def __init__(self, size=0):
        """Method that stores the size of the square
        Attributes:
            __size (int): size of square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = int(size)