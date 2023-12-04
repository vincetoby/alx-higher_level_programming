#!/usr/bin/python3
"""
method module
"""


def is_kind_of_class(obj, a_class):
    """check if object is instance of specificed class
    args:
        obj: object
        a_class: class type
    Return:
        True or False
    """

    return isinstance(obj, a_class)
