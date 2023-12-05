#!/usr/bin/python3
"""
Class Module
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """a subclass Rectangle """

    def __init__(self, width, height):
        """initialization method"""
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height

    def area(self):
        """func that calculates area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """print method"""
        return "[{}] {}/{}".format(__class__.__name__,
                                   self.__width, self.__height)
