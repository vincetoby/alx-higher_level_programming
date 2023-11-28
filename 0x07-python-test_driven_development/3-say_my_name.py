#!/usr/bin/python3
"""
    defines na function that prints full name

    Args:
        first_name: first name
        last_name: last name

    Raise:
        TypeError: first_name and last_name must be strings

"""


def say_my_name(first_name, last_name=""):
    """prints first and last name"""
    err_msg = "first_name must be a string or last_name must be a string"
    if type(first_name) is not str or type(last_name) is not str:
        raise TypeError(err_msg)
    print("My name is {} {}".format(first_name, last_name))
