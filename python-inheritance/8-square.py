#!/usr/bin/python3
"""
This module defines a Square class that inherits from Rectangle.
"""


class BaseGeometry:
    """
    Geometry base class with validation.
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


class Rectangle(BaseGeometry):
    """
    Rectangle class with full functionality.
    """

    def __init__(self, width, height):
        """
        Initialize a Rectangle instance.

        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle (width * height)
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Return string representation of the rectangle.

        Returns:
            str: Rectangle description in format [Rectangle] <width>/<height>
        """
        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(Rectangle):
    """
    Square class that inherits from Rectangle.

    A square is a special case of rectangle where width equals height.
    """

    def __init__(self, size):
        """
        Initialize a Square instance.

        Args:
            size (int): The size of the square (both width and height)
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
