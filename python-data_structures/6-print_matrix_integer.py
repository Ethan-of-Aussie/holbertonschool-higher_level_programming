#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for inner in matrix:
        if len(inner) == 0:
            print()
            continue
        for j, val in enumerate(inner):
            if j < len(inner) - 1:
                print("{:d}".format(val), end=" ")
            else:
                print("{:d}".format(val))
