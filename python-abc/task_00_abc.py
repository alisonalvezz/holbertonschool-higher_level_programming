#!/usr/bin/python3
"""
abstract class
"""


from abc import ABC, abstractmethod

class Animal(ABC):
    """ abstract class animal"""

    @abstractmethod
    def sound(self):
        """sound"""
        pass

class Dog(Animal):
    """
    subclase dog
    """

    def sound(self):
        """
        returns bark
        """

        return 'Bark'
    
class Cat(Animal):
    """
    subclass cat
    """

    def sound(self):
        """
        returns Meow
        """

        return 'Meow'
        