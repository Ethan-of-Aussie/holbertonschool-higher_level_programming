#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newmatrix = list(map(lambda row: list(map(lambda x: x * x, row)), matrix))
    return newmatrix
