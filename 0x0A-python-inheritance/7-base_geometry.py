#!/usr/bin/python3
"""
This module defines the class BaseGeometry.
"""


class BaseGeometry:
    """
    A class representing base geometry.
    """
    def area(self):
        """
        Public instance method that raises an exception indicating
        that the method is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that the input `value` is a positive integer.

        Args:
            name (str): The name associated with the value.
            value (int): The value to validate.

        Raises:
            TypeError: If `value` is not an integer.
            ValueError: If `value` is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
