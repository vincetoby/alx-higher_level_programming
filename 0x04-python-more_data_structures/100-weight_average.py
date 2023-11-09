#!/usr/bin/python3
def p_promedium(scores):
    list_proms = list(map(lambda a: a[0] * a[1], scores))
    return sum(list_proms)


def sum_weight(scores):
    list_w = list(map(lambda a: a[1], scores))
    return sum(list_w)


def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    else:
        av = p_promedium(my_list) / sum_weight(my_list)
        return av
