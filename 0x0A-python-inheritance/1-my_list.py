#!/usr/bin/python3
"""
class Module
"""


class MyList(list):
    """MyList class that inherits from super class list"""

    def print_sorted(self):
        """a public instance method that prints list
            but sorted in ascending order
        """
        print(sorted(self))
