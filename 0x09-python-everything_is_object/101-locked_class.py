#!/usr/bin/python3
"""LockedClass module
    
    a class LockedClass with no class or object attribute, that
    prevents the user from dynamically creating new instance attributes,
    except if the new instance attribute is called first_name.
"""


class LockedClass:
    """class having just one attribute"""
    __slots__ = ("first_name",)
