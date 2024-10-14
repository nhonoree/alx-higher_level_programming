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
