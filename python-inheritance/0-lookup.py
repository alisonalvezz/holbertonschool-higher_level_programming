#!/usr/bin/python3
"""
prints a list of available attributes and methods of an object
"""


def lookup(obj):
    """
    returns the object and its attributes
    """
    return dir(obj)
