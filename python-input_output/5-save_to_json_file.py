#!/usr/bin/python3
"""
writes an object to a text file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    writes an object to a text file
    using a json representation
    """

    with open(filename, 'w') as file:
        json.dump(my_obj, file)
