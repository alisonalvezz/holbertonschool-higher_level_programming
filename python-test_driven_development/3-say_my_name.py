#!/usr/bin/python3
"""
prints a name
"""


def say_my_name(first_name, last_name=""):
    """
    function that prints a name

    Args:
        first_name: first name of the name
        last_name: last name of the name

    Raises:
        TypeError: if first name or last name are not strings
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
