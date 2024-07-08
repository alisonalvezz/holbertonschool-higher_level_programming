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
        initializes the rectangle
        Attributes:
            Width: the width of the rectangle
            Height: the height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        the width of the rectangle
        Attributes:
            Value: value of the width
        Raises:
            TypeError: if width isnt an integer
            ValueError: if width is negative
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Defines height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Height of the rectangle
        Attributes:
            Value: value of the height
        Raises:
            TypeError: if value isnt an integer
            ValueError: if height is a negative
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        the  area of the rectangle
        Returns:
            Width multiplied by height
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        the perimeter of the rectangle
        Returns:
            2 multiplied by the sum of width and height
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)
