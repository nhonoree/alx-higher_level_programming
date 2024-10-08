#!/usr/bin/python3
def print_square(size):
    """Prints a square with the character '#' of the given size."""

    # Check if size is an integer
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    # Check if size is non-negative
    if size < 0:
        raise ValueError("size must be >= 0")

    # Print the square
    for _ in range(size):
        print("#" * size)
