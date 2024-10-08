#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    """Prints 'My name is <first name> <last name>'."""

    # Ensure first_name and last_name are strings
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    # Print the name
    print(f"My name is {first_name} {last_name}")
