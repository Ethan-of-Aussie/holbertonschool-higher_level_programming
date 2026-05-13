#!/usr/bin/python3
def search_replace(my_list, search, replace):
    newlist = my_list[:]
    for i, val in enumerate(my_list):
        if val == search:
            newlist[i] = replace
    return newlist
