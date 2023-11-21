#!/usr/bin/python3
"""Defines a class 'square' with a private instance attribute"""


class Square:
    """Definition of class"""
    def __init__(self, size=0):
        """Init Square with a private instance attr 'size'

            Args:
                size: An integer and size of the square.

            Raises:
                TypeError: The size arg isn't an integer.
                ValueError: The size arg is less than zero(negative).
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
