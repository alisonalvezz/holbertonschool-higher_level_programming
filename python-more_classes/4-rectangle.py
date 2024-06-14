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
        initializes width and height
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
            Value: value of the width
        Raises:
            TypeError: if value isnt an integer
            ValueError: if value is a negative
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
            Value: value of the height of the rectangle
        Raises:
            TypeError: if value isnt an integer
            ValueError: if value is a negative
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        the area of the rectangle
        Returns:
            the multiplication btw the width and the height
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        the perimeter of the rectangle
        Returns:
            the sum of width and height mul by 2
        """
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns a string representation of the Rectangle object.

        If either the width (__width) or the height (__height) of the rectangle
        is 0, returns an empty string.

        Returns:
            str: A string representation of the rectangle using '#' characters
                to represent each row and column.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(["#" * self.__width for _ in range(self.__height)])

    def __repr__(self):
        """
        Returns a string representation of the Rectangle object for debugging.

        Returns:
        str: A string that includes the class name and the current values
        of width (__width) and height (__height) of the rectangle.
        """
        return f"Rectangle({self.__width}, {self.__height})"
