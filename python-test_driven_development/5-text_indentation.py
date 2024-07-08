#!/usr/bin/python3
"""
text indentation
"""


def text_indentation(text):
    """
    Indents a text based on specific punctuation marks.

    Args:
        text (str): The text to be indented.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuation = [":", "?", "."]

    for i in punctuation:
        text = (i + "\n\n").join([j.strip(" ") for j in text.split(i)])

    print(f"{text}", end='')
