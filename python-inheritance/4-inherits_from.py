#!/usr/bin/python3
"""
a function
"""


def inherits_from(obj, a_class):
    """
    returns true if the object is an instance of a class 
    that inherited from the specified class else returns false
    """
    if isinstance(obj, a_class) and issubclass(a_class, a_class):
            return True
    else:
        return False
