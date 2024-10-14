#!/usr/bin/python3
"""
This module contains the function is_kind_of_class.
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance of, or if the object is an
    instance of a class that inherited from, the specified class.
    
    :param obj: The object to check.
    :param a_class: The class to check against.
    :return: True if obj is an instance or inherited instance of a_class,
             False otherwise.
    """
    return isinstance(obj, a_class)
