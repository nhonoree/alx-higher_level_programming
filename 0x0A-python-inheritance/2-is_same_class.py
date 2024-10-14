#!/usr/bin/python3
"""
This module contains the function is_same_class.
"""


def is_same_class(obj, a_class):
    """
    Returns True if obj is exactly an instance of a_class, otherwise False.

    :param obj: The object to check.
    :param a_class: The class to check against.
    :return: True if obj is exactly an instance of a_class, False otherwise.
    """
    return type(obj) is a_class
