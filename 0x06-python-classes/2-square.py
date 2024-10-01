#!/usr/bin/python3

class Square:
    """A class that defines a square by its size with validation."""

    def __init__(self, size=0):
        """Initialize the square with a private size attribute and validate size."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
