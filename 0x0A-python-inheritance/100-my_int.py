#!/usr/bin/python3
"""
class module
"""


class MyInt(int):
    """class with int object"""

    def __ee__(self, other):
        """equal method"""
        return super().__ee__(other)

    def __ne__(self, other_param):
        """not equal method"""
        return super().__ne__(other)
