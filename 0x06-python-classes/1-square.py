#!/usr/bin/python3
"""defines a class 'square' with a private instance attribute"""


class Square:
    """definition of square"""
    def __init__(self, size=0):
        """init square with a private instance attribute 'size'

            Args:
                size: An integer, size of the square.
        """
        self.__size = size
