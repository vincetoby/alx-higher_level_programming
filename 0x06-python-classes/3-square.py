#!/usr/bin/python3
"""Defines a class 'square' with a private instance attribute."""


class Square:
    """Definition of the class"""
    def __init__(self, size=0):
        """Init Square with 'size' integer.

            Args:
                size: An integer, size of the square.

            Raises:
                TypeError: The size args is not an integer.
                ValueError: The size args is negative.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """a Public instance method that computes the area of the square."""
        return self.__size * self.__size
