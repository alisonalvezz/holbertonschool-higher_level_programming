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
    lines = []
    line = ""

    for char in text:
        line += char
        if char in punctuation:
            lines.append(line.strip() + "\n\n")
            line = ""

    if line:
        lines.append(line.strip())

    for line in lines:
        print(line)
