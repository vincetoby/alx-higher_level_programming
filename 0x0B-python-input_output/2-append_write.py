#!/usr/bin/python3
"""method module"""

def append_write(filename="", text=""):
    """append text to file"""
    with open(filename, "a", encoding="utf-8") as op:
        return op.write(text)
