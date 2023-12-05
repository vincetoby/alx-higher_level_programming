#!/usr/bin/python3
"""
class module
"""


class BaseGeometry:
    """a class BaseGeometry with public inst method area"""

    def area(self):
        """raises an exception if area isn't implemented"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """check if value is an integer"""
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
