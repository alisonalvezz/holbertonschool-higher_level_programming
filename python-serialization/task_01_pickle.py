#!/usr/bin/python3

import pickle

"""
uses pickle to serialize and deserialize
"""

class CustomObject:
    """
    the custom object
    """
    def __init__(self, name, age, is_student):
        """
        initializes attributes
        Attributes:
            Name
            Age
            Is student
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        displays the name, age and if is student
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")


    def serialize(self, filename):
        """
        serialization with pickle
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except (pickle.PickleError, IOError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        deserialization
        """
        try:
            with open(filename, 'rb') as file:
                obj = pickle.load(file)
                if isinstance(obj, CustomObject):
                    return obj
                else:
                    return None
        except (pickle.PickleError, IOError):
            return None
