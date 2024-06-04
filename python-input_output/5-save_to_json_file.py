#!/usr/bin/python3
"""
writes an object to a text file
"""


import json

def save_to_json_file(my_obj, filename):
    """
    writes an object to a text file
    using a json representation
    Attributes:
        my_obj: the object to a text file
        filename: the text file
    """

    with open(filename, 'w') as file:
        json.dump(my_obj, file)
