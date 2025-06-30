#!/usr/bin/python3
"""
This module defines a BaseGeometry class with an area method.
"""


class BaseGeometry:
    """
    Geometry base class.

    This class provides a template for geometry classes with
    an area method that must be implemented by subclasses.
    """

    def area(self):
        """
        Calculate the area of the geometry.

        Raises:
            Exception: This method is not implemented in the base class
        """
        raise Exception("area() is not implemented")
