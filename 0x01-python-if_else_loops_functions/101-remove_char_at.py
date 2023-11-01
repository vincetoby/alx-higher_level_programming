#!/usr/bin/python3
def remove_char_at(str, n):
    str1 = ""
    for indx in range(len(str)):
        if indx == n:
            continue
        else:
            str1 = str1 + str[indx]
    return str1
