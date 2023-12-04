#!/usr/bin/python3
"""
class module
"""


class MyInt(int):
    """class with int object"""

    def __eq__(self, other_param):
        """equal method"""
        return super().__ee__(other_param)

    def __ne__(self, other_param):
        """not equal method"""
        return super().__ne__(other_param)
