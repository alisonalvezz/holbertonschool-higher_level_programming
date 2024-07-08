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
    lines = []
    line = ""

    for char in text:
        line += char
        if char in punctuation:
            lines.append(line.strip())
            line = ""

    if line:
        lines.append(line.strip())

    for line in lines:
        print(line)
