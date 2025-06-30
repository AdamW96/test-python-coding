#!/usr/bin/python3
"""
This module provides a function to check if an object is an instance
of a class that inherited from the specified class.
"""


def inherits_from(obj, a_class):
    """
    Check if object is an instance of a class that inherited from a_class.

    Args:
        obj: The object to check
        a_class: The class to check against

    Returns:
        bool: True if obj inherits from a_class (but is not exactly a_class)
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
