#!/usr/bin/python3
"""
function that returns true if an object is an instance of a class or
if an object is an instance of a class that inherited from the specified class
otherwise, it returns false
"""


def is_kind_of_class(obj, a_class):
    if isinstance(obj, a_class) and issubclass(a_class, a_class):
            return True
    else:
          return False