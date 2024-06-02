#!/usr/bin/python3
"""
based on "6-based_geometry.py"
"""


class BaseGeometry:
    """
    function based on 6-based_geometry.py

    Raises:
        Exception: for area, that isnt implemented
        TypeError: if value isnt an integer
        ValueError: if value isnt greater than 0
    """
    def area(self):
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        self.name = name
        self.value = value

        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
