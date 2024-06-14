#!/usr/bin/python3


class Square:
    """Define a class square

    Attributes:
        __size (int): size of the square
    """
    def __init__(self, size=0):
        """Initializes the square with a given size

        Attributes:
            __size (int): size of square

        Raises:
            TypeError: if size isnt an integer
            ValueError: if size is negative
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = int(size)

    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The area of the square (size ** 2).
        """
        return self.__size ** 2
