#!/usr/bin/python3

"""
defines a rectangle
"""


class Rectangle:
    """
    defines a rectangle
    """
    def __init__(self, width=0, height=0):
        """
        initializes the width and height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        the width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        the width of the rectangle
        Attributes:
            Value: the value of the width
        Raises:
            TypeError: if width isnt an integer
            ValueError: if width is a negative
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Height of the rectangle
        Attributes:
            Value: value of the height
        Raises:
            TypeError: if height isnt an integer
            ValueError: if height is a negative
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Area of the rectangle
        Returns:
            width multiplied by height (the area)
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Perimeter of the rectangle
        Returns:
            the sum of width and height multiplied by 2
        """
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns a string representation of the object.

        Returns a string that represents the rectangle using the '#' character
        for each row and column that makes up the rectangle.

        Returns an empty string if the width or height of the rectangle is 0.

        Returns:
            str: String representation of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(["#" * self.__width for _ in range(self.__height)])
