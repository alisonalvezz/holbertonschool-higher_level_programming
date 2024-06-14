#!/usr/bin/python3
"""
defines a rectangle
"""


class Rectangle:
    """
    defines a rectangle
    Attributes:
        width: width of the rectangle
        height: height of the rectangle
    Raises:
        TypeError: when the width or height arent int
        ValueError: when widht or height are negative
    """
    def __init__(self, width=0, height=0):
        """
        Initializes the rectangle with width and height

        Attributes:
            Width: the width of the rectangle
            Height: the height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        width of the rectangle
        Attributes:
            Value: the value of the width
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
