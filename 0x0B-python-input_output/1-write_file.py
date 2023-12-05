#!/usr/bin/python3
"""method module
"""


def write_file(filename="", text=""):
    """writes file"""
    with open(filename, "w", encoding="UTF-8") as op:
        return op.write(text)
