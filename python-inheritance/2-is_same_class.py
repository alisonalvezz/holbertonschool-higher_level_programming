#!/usr/bin/python3
"""
a function that returns false if the object isnt an instance
of a determined class, otherwise it returns true
"""


def is_same_class(obj, a_class):
    if not isinstance(obj, a_class):
        return False
    else:
        return True
