#!/usr/bin/python3


import json


def save_to_json_file(my_obj, filename):
    with open(filename, "w", encoding="UTF-8") as op:
        json.dump(my_obj, op)
