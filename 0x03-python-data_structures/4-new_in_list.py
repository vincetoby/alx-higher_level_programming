#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = my_list[:]  # without [:] there wd be issues
    if idx < 0 or idx > len(new_list) - 1:
        return new_list
    else:
        new_list[idx] = element
        return new_list
