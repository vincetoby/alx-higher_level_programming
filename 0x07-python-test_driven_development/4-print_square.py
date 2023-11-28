#!/usr/bin/python3
"""
    defines a function that prints a square using
    the character #.

    Args:
        size: length/width of the square

    Raise:
        TypeError: size must be an integer
        TypeError:   
        ValueError:

    size must be an integer, otherwise raise a TypeError
    exception with the message size must be an integer

    if size is less than 0, raise a ValueError exception
    with the message size must be >= 0

    if size is a float and is less than 0,
    raise a TypeError exception with the message size
    must be an integer
"""


def print_square(size):
    """ prints a square with '#' """
    err_msg1 = "size must be an integer"
    err_msg2 = "size must be >= 0"
    if type(size) is not int:
        raise TypeError(err_msg1)
    if size < 0:
        raise ValueError(err_msg2)
    for i in range(size):
        print("#" * size, end="")
        print()
