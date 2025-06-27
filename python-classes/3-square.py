#!/usr/bin/python3
"""
This module defines a Square class with property-based access.

The Square class uses properties to provide controlled access to the
private size attribute with validation.
"""


class Square:
    """
    A class that defines a square with property-based attribute access.

    This class uses Python properties to provide controlled access to
    the private size attribute while maintaining validation.
    """

    def __init__(self, size=0):
        """
        Initialize a new Square instance.

        Args:
            size (int): The size of the square, defaults to 0
        """
        self.size = size  # This calls the setter

    @property
    def size(self):
        """
        Get the size of the square.

        Returns:
            int: The current size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square with validation.

        Args:
            value (int): The new size value

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
            int: The area of the square (size * size)
        """
        return self.__size * self.__size
