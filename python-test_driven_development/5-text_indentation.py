#!/usr/bin/python3
"""
indents a text
"""
def text_indentation(text):
    """
    indents a text

    Args:
        text: text to be indented

    Raises:
        TypeError: if text isnt a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuation = [":", "?", "."]
    for char in text:
        print(char, end="")
        if char in punctuation:
            print("\n")
