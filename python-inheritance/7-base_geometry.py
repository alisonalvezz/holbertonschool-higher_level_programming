#!/usr/bin/python3
"""
based on "6-based_geometry.py"
"""


class BaseGeometry:
    """
    function based on 6-based_geometry.py

    Methods:
        area(self): raises an exception with a message that says
                    that area is not implemented yet
        integer_validator(self, name, value): validates that value
                    is an integer and greater than 0

    Raises:
        Exception: for area, that isnt implemented
        TypeError: if value isnt an integer
        ValueError: if value isnt greater than 0
    """
    def area(self):
        """
        area is not implemented
        """
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """
        integer validator
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
