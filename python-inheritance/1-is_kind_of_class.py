#!/usr/bin/python3
"""
This module provides a function to check if an object is an instance
of a specified class or inherits from it.
"""


def is_kind_of_class(obj, a_class):
    """
    Check if object is an instance of, or inherits from, the specified class.

    Args:
        obj: The object to check
        a_class: The class to check against

    Returns:
        bool: True if obj is an instance of a_class or inherits from it
    """
    return isinstance(obj, a_class)
