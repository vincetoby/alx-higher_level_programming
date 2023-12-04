#!/usr/bin/python3
"""
method module
"""


def lookup(obj):
    """Lookup all avail attributes in object

    Args:
        obj: object for lookup
    Return:
        list of attributes
    """
    # dir() returns a list of attributes
    return [attr for attr in dir(obj)]
