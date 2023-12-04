#!/usr/bin/python3
"""
a method module
"""


def add_attribute(obj, obj_name, obj_value):
    """add a new attribute to an bject

    args:
        obj: class object
        obj_name: object name
        obj_value: value of attribute

    """
    if hasattr(obj, "__dict__") == False:
        raise TypeError("can't add new attribute")
    setattr(obj, obj_name, obj_value)
