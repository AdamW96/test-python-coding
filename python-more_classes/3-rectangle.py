#!/usr/bin/python3
"""
This module defines a Rectangle class with eval-compatible representation.

The Rectangle class provides both string representation for visualization
and repr representation for object recreation.
"""


class Rectangle:
    """
    A class that defines a rectangle with complete representation methods.

    This class provides both __str__ for human-readable output and __repr__
    for developer-friendly representation that can recreate the object.
    """

    def __init__(self, width=0, height=0):
        """
        Initialize a new Rectangle instance.

        Args:
            width (int): The width of the rectangle, defaults to 0
            height (int): The height of the rectangle, defaults to 0
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Get the width of the rectangle.

        Returns:
            int: The current width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle with validation.

        Args:
            value (int): The new width value

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Get the height of the rectangle.

        Returns:
            int: The current height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle with validation.

        Args:
            value (int): The new height value

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculate and return the area of the rectangle.

        Returns:
            int: The area of the rectangle (width * height)
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculate and return the perimeter of the rectangle.

        If width or height is 0, perimeter is 0.

        Returns:
            int: The perimeter of the rectangle (2 * (width + height))
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Return a string representation of the rectangle using '#' characters.

        If width or height is 0, returns an empty string.

        Returns:
            str: Visual representation of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        rectangle_lines = []
        for i in range(self.__height):
            rectangle_lines.append("#" * self.__width)

        return "\n".join(rectangle_lines)

    def __repr__(self):
        """
        Return a string representation that can recreate the object.

        This representation can be used with eval() to create a new
        Rectangle instance with the same width and height.

        Returns:
            str: Official string representation of the rectangle
        """
        return f"Rectangle({self.__width}, {self.__height})"
