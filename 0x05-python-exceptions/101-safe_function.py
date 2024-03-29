#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        p = fct(*args)
    except Exception as ex:
        print("Exception:", ex, file=sys.stderr)
        return None
    return p
