#!/usr/bin/python3
"""
based on "7-based_geometry.py"
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class that inherits from BaseGeometry
    instantiation with width and height:
    def __init__(self, width, height):
        width and height must be private
        width and height must be positive integers
    """

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__heigth = height