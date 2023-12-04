#!/usr/bin/python3
"""
class module
"""


class BaseGeometry:
    """a class BaseGeometry with public inst method area"""

    def area(self):
        """raises an exception if area isn't implemented"""
        raise Exception('area() is not implemented')
