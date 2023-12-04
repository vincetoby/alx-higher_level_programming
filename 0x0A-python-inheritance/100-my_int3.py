#!/usr/bin/python3
"""
class module
"""


class MyInt(int):
    """class with int object"""

    def __eq__(self, other):
        """equal method"""
        return super().__eq__(other)

    def __ne__(self, other_param):
        """not equal method"""
        return super().__ne__(other)
