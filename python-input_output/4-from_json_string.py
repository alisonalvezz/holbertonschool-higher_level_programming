#!/usr/bin/python3
"""
returns an object represented by a json string
"""


import json


def from_json_string(my_str):
    """
    function that returns an object that is
    represented by a json string
    Attributes:
        my_str: the string to be represented
    """

    return json.loads(my_str)
