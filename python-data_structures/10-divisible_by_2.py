#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    isisnt = []
    for i in my_list:
        if i % 2 == 0:
            isisnt.append(True)
        else:
            isisnt.append(False)
    return isisnt
