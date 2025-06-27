#!/usr/bin/python3
"""
This module defines a Square class with size validation.

The Square class represents a square with a validated private size attribute.
"""


class Square:
    """
    A class that defines a square with size validation.

    This class represents a square with a private size attribute that
    undergoes type and value validation during initialization.
    """

    def __init__(self, size=0):
        """
        Initialize a new Square instance with validation.

        Args:
            size (int): The size of the square, defaults to 0

        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
