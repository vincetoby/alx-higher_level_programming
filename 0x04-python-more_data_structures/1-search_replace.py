#!/usr/bin/python3
def search_replace(my_list, search, replace):
    dope = [fig if fig != search else replace for fig in my_list]
    return dope
