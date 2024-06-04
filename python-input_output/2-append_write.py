#!/usr/bin/python3
"""
appends a string at the end of a text file
"""


def append_write(filename="", text=""):
    with open(filename, 'a', encoding='UTF8') as file:
        return file.write(text)