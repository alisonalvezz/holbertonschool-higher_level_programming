#!/usr/bin/python3

import json

"""
serializes and deserializes data
"""


def serialize_and_save_to_file(data, filename):
    """
    serializes data in filename
    """
    with open(filename, 'w') as file:
        json.dump(data, file)

def load_and_deserialize(filename):
    """
    deserializes data from filename
    """
    with open(filename, 'r') as file:
        json.load(file)
