#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    dopple = []
    for row in matrix:
        dopp_matrix = map(lambda i: i**2, row)
        dopple.append(list(dopp_matrix))
    return dopple
