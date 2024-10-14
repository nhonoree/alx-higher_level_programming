#!/usr/bin/python3
"""Defines a class MyList that inherits from list."""

class MyList(list):
    """A subclass of list with an additional method to print sorted list."""
    
    def print_sorted(self):
        """Prints the list in ascending order."""
        print(sorted(self))
