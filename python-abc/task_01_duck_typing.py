#!/usr/bin/python3
"""
duck typing
"""


from abc import ABC, abstractmethod
import math

class Shape(ABC):
    """
    area and perimeter
    """

    @abstractmethod
    def area(self):
        """
        area shape
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        perimeter shape
        """
        pass


class Circle(ABC):
    def __init__(self, radius):
        """
        init class
        """
        self.radius = abs(radius)

    def area(self):
        """
        return of area
        """
        return math.pi * (self.radius ** 2)
    
    def perimeter(self):
        """
        return of perimeter
        """

        return 2 * math.pi * self.radius
    

class Rectangle(ABC):
    """
    Rectangle
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """
        area returns
        """
        return self.width * self.height
    
    def perimeter(self):
        """
        perimeter returns
        """
        
        return 2 * (self.width + self.height)
    
def shape_info(info):
    """
    info to print
    """

    print(f"Area: {info.area()}")
    print(f"Perimeter: {info.perimeter()}")
