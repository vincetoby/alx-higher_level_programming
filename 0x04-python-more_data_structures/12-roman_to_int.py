#!/usr/bin/python3
digits = ["IX", "VIII", "VII", "VI", "V",
          "IV", "III", "II", "I"]
hundreds = ["CM", "DCCC", "DCC", "DC", "D",
            "CD", "CCC", "CC", "C"]
tens = ["XC", "LXXX", "LXX", "LX", "L",
        "XL", "XXX", "XX", "X"]
thousands = ["MMM", "MM", "M"]


def digitcheck(strg, fig):
    max_match = ""
    for i in fig:
        if i in strg and len(i) > len(max_match):
            max_match = i
        if max_match:
            return list(reversed(fig)).index(max_match) + 1
    return -1


def convert_rom(string):
    thousand = digitcheck(string, thousands)
    if thousand != -1:
        change = thousands[thousand - 1]
        string = string.replace(change, '')
    else:
        thousand = 0
    hundred = digitcheck(string, hundreds)
    if hundred != -1:
        change = hundreds[hundred - 1]
        string = string.replace(change, '')
    else:
        hundred = 0
    ten = digitcheck(string, tens)
    if ten != -1:
        change = tens[ten - 1]
        string = string.replace(change, '')
    else:
        ten = 0
    digit = digitcheck(string, digits)
    if digit != -1:
        change = digits[digit - 1]
        string = string.replace(change, '')
    else:
        digit = 0
    return thousand * 1000 + hundred * 100 + ten * 10 + digit


def check_in(string):
    for indx in string:
        if indx not in 'MCDLXVI':
            return False
    return True


def roman_to_int(roman_string):
    if roman_string is None:
        return 0
    if not isinstance(roman_string, str):
        return 0
    if not check_in(roman_string):
        return 0
    data = convert_rom(roman_string)
    return data
