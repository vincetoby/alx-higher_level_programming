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

    @property
    def size(self):
        """gets size of the square

        Returns:
            The size private instance attribute of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size to a value

        Args:
            value: value to be assigned to size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def __lt__(self, other):
        """Computes comparison of self < other"""
        return self.__size < other.__size

    def __le__(self, other):
        """Computes comparison of self <= other"""
        return self.__size <= other.__size

    def __eq__(self, other):
        """Computes comparison of self == other"""
        return self.__size == other.__size

    def __ne__(self, other):
        """Computes comparison of self != other"""
        return self.__size != other.__size

    def __gt__(self, other):
        """Computes comparison of self > other"""
        return self.__size > other.__size

    def __ge__(self, other):
        """Computes comparison of self >= other"""
        return self.__size >= other.__size
