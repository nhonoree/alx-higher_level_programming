#!/usr/bin/python3
"""
This module contains the function inherits_from.
"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class; otherwise False.
    
    :param obj: The object to check.
    :param a_class: The class to check inheritance from.
    :return: True if obj is an inherited instance of a_class, False otherwise.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
