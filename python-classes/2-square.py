#!/usr/bin/python3
class Square:
    """
    define a class square
    """
    def __init__(self, size=0):
        """
        method that stores the size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        """
        if size isnt an int
        """
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = int(size)

