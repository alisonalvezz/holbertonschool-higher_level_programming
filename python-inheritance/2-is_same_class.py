#!/usr/bin/python3
"""
a function
"""


def is_same_class(obj, a_class):
    """
    returns flase if the object isnt an instance
    of a class
    otherwise returns true
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
