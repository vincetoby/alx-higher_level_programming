#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    first = sentence[0] if length > 0 else "None"
    rval = length, first
    return rval
