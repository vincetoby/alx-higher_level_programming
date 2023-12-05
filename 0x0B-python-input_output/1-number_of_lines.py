#!/usr/bin/python3
"""
method module
"""


def number_of_lines(filename=""):
    """number of lines from file
    args:
        filename: file to read
    return:
        number of lines
    """
    line_numb = 0
    with open(filename, encoding="utf-8") as op:
        for line in op:
            line_numb += 1
    return line_numb
