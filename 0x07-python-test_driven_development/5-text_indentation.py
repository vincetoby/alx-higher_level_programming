#!/usr/bin/python3
"""
    a function that prints a text with 2 new lines after each
    of these characters: ., ? and :

    Args:
        text: a string

    Raise:
        TypeError: text must be a string

"""


def text_indentation(text):
    """prints aa text with 2 new lines after specified chars"""
    err_msg = "text must be a string"
    new = ""
    fg = False
    if type(text) is not str:
        raise TypeError(err_msg)
    new = text.replace(". ", ".")
    new = new.replace(": ", ":")
    new = new.replace("? ", "?")
    for charac in new:
        if charac in [".", "?", ":"]:
            print(charac)
            print()
            fg = True
        else:
            if fg is False:
                print(charac, end="")
            else:
                if charac != " ":
                    print(charac, end="")
                    fg = False
