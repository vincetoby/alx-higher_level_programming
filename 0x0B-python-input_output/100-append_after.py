#!/usr/bin/python3
"""append_after"""


def append_after(filename="", search_string="", new_string=""):
    """search and update"""
    read = []
    with open(filename, "r", encoding="utf-8") as opened_file:
        read_file = opened_file.readlines()
        indx = 0

        while indx < len(read_file):
            if search_string in read_file[indx]:
                read_file[indx:indx + 1] = [read_file[indx], new_string]
                indx += 1
            indx += 1

    with open(filename, "w", encoding="utf-8") as file:
        file.writelines(read_file)
