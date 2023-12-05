#!/usr/bin/python3
"""method module
"""


import json


def load_from_json_file(filename):
    """creates an Object from a “JSON file"""
    with open(filename, "r", encoding="UTF-8") as op:
        return json.load(op)
