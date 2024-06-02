#!/usr/bin/python3
"""
function that returns true if the object is an instance of a class
that inherited from the specified class
else returns false
"""


def inherits_from(obj, a_class):
    if isinstance(obj, a_class) and issubclass(a_class, a_class):
            return True
    else:
        return False
