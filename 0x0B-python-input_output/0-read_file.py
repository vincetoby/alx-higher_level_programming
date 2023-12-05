#!/usr/bin/python3
"""method module
"""

def read_file(filename=""):
    """reads file"""
    with open(filename, "r", encoding="UTF-8") as opened_file:
        print(opened_file.read(), end="")
