#!/usr/bin/python3
"""defines a func that adds ints
        Args:
            a: first int/float
            b: second int/float

        Raise:
            TypeError: a and b must be an integer/float

        Return:
            value of addition of a and b

"""


def add_integer(a, b=98):
    """adds two integers"""
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    if isinstance(b, float):
        b = int(b)
    if isinstance(a, float):
        a = int(a)
    return (a + b)
