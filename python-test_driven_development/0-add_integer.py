#!/usr/bin/python3
""" This module is composed by a function that adds two numbers
"""


def add_integer(a, b=98):
    """
    function that adds two numbers
    
    Args:
        a: first number
        b: second number
    
    Returns:
        the addition of the two numbers

    Raises:
        TypeError if a or b arent integers
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    b = int(b)
    return(a + b)
