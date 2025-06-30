#!/usr/bin/python3
"""
This module defines a BaseGeometry class with validation methods.
"""


class BaseGeometry:
    """
    Geometry base class with validation.

    This class provides area calculation template and integer validation.
    """

    def area(self):
        """
        Calculate the area of the geometry.

        Raises:
            Exception: This method is not implemented in the base class
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate that a value is a positive integer.

        Args:
            name (str): The name of the value being validated
            value: The value to validate

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than or equal to 0
        """
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
