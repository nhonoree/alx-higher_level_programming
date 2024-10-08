#!/usr/bin/python3
def text_indentation(text):
    """Prints text with 2 new lines after each of '.', '?', and ':'."""

    # Check if text is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Initialize a variable to store the formatted result
    formatted_text = ""

    # Loop through the text and insert new lines after the specified characters
    for char in text:
        formatted_text += char
        if char in ".?:":
            formatted_text += "\n\n"

    # Print the formatted text without extra spaces
    print("\n".join(line.strip() for line in formatted_text.splitlines()))
