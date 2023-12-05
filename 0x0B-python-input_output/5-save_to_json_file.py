#!/usr/bin/python3
"""method module
"""


import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation"""
    with open(filename, "w", encoding="UTF-8") as op:
        json.dump(my_obj, op)
