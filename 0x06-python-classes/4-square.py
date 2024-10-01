#!/usr/bin/python3

class Square:
    """A class that defines a square with size validation, area calculation, and property for size."""

    def __init__(self, size=0):
        """Initialize the square and validate size."""
        self.size = size  # This will use the setter

    @property
    def size(self):
        """Retrieve the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square area."""
        return self.__size ** 2
