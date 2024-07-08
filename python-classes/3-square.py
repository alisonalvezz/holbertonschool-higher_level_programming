#!/usr/bin/python3

class Square:
    """Defines a Square
    Attributes:
        __size (int): size of the square
    """
    def __init__(self, size=0):
        """
        Initializes the square with a size
        Args:
            size(int): Size of the square (default is 0)

        Raises:
            TypeError: If size is not an integer
            ValueError: If size is negative
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """
        Calculates and returns the area of the square

        Returns:
            int: the area of the square (size ** 2)
        """
        return self.__size ** 2
