#!/usr/bin/python3
"""
a function
"""


def inherits_from(obj, a_class):
    """
    returns true if the object is an instance of a class 
    that inherited from the specified class else returns false
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
