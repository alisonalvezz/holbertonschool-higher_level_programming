#!/usr/bin/python3
"""
writes a string to a text file 
"""


def write_file(filename="", text=""):
    """
    open file and returns the number of
    characters written
    """
    with open(filename, 'w', encoding='UTF8') as file:
        return file.write(text)