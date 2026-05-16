#!/usr/bin/python3


def roman_to_int(roman_string):
    romnum = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0

    if not isinstance(roman_string, str):
        return 0
    for key in range(len(roman_string)):
        curchar = roman_string[key]
        curval = romnum[curchar]

        if key + 1 < len(roman_string):
            nextchar = roman_string[key + 1]
            nextval = romnum[nextchar]

            if nextval > curval:
                total -= curval
            else:
                total += curval
        else:
            total += curval
    return total
