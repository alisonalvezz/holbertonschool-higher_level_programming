#!/usr/bin/python3
"""
based on "6-based_geometry.py"
"""

class BaseGeometry:
    def area(self):
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        self.name = name
        self.value = value

        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
