#!/usr/bin/python3
"""
Method module
"""


def is_same_class(obj, a_class):
    """checks if obj is of type a_class
    args:
        obj: object to check
        a_class: class type
    Return:
        True or False
    """

    if type(obj) is a_class:
        return True
    else:
        return False
