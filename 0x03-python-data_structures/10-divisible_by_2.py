#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    tp = []
    for i in my_list:
        if i % 2 == 0:
            tp.append(True)
        else:
            tp.append(False)
    return tp
