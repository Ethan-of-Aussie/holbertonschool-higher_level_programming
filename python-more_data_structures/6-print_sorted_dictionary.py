#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    diccopy = a_dictionary.copy()
    print("\n".join(map(lambda k: f"{k}: {diccopy[k]}", sorted(diccopy))))
