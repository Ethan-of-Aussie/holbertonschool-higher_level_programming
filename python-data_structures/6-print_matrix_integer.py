#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i, inner in enumerate(matrix):
        for j, val in enumerate(inner):
            print("{:d}".format(val), end=" ")
        print()
