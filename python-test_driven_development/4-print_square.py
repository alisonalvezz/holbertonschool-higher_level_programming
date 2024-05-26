#!/usr/bin/python3
"""
prints a square
"""
def print_square(size):
    """
    prints a square

    Args:
        size: length of the square

    Raises:
        TypeError: if size isnt an integer or less than zero
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise TypeError("size must be >= 0")
    
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
