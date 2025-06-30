#!/usr/bin/python3

class Square:
    """
    A class that defines a square.

    This class represents a square with a private size attribute.
    The size is kept private to maintain control over its value.
    """

    def __init__(self, size):
        """
        Initialize a new Square instance.

        Args:
            size: The size of the square (no type/value verification)
        """
        self.__size = size
