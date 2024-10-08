#!/usr/bin/python3
def add_integer(a, b=98):
    """
    Adds two integers or floats, after converting them to integers.

    Args:
        a: The first number (int or float).
        b: The second number (int or float), defaults to 98.

    Returns:
        The sum of the two integers.

    Raises:
        TypeError: If either a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Convert floats to integers before addition
    return int(a) + int(b)
