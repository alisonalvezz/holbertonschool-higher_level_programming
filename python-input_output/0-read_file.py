#!/usr/bin/python3
"""
reads a text file
"""


def read_file(filename=""):
    """
    open file and read
    """
    with open(filename, encoding='UTF8') as file:
        print(file.read())
