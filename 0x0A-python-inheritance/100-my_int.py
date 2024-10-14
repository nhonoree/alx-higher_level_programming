#!/usr/bin/python3
"""Defines a class MyInt that inherits from int and inverts == and != operators."""

class MyInt(int):
    """Represents a rebel integer that inverts == and != operators."""

    def __eq__(self, other):
        """Override the == operator with != behavior."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Override the != operator with == behavior."""
        return super().__eq__(other)
