#!/usr/bin/python3
"""
Method module
"""


def inherits_from(obj, a_class):
    """returns True if the object is an instance of a
        class that inherited (directly or indirectly) 
        from the specified class 
    args:
        obj: object to access
        a_class: class type
    returns:
        True or False
    """
    if type(obj) is a_class:
        return False
    return issubclass(type(obj), a_class)
