#!/usr/bin/python3
"""
This module defines a Square class with printing capability.

The Square class provides methods to calculate area and print the square
using the '#' character.
"""


class Square:
    """
    A class that defines a square with printing capability.

    This class provides complete square functionality including
    size validation, area calculation, and visual representation.
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

    def my_print(self):
        """
        Print the square using '#' characters.

        If size is 0, prints an empty line.
        Otherwise, prints a square pattern of '#' characters.
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
