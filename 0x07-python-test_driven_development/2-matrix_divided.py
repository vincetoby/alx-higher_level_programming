#!/usr/bin/python3
"""defines a func for  matrix division
         Args:
            matrix(list of lists): list containing elements to divide
            div(float):divisor

        Raise:
            TypeError: matrix must be a list of lists of integers or floats
            TypeError: Each row of the matrix must be of the same size
            TypeError: div must be a number (integer or float)
            ZeroDivisionError:div can’t be equal to 0

        Return:
            a new matrix with every element divided

"""


def matrix_divided(matrix, div):
    """divides every element of matrix"""

    errrMsg = "matrix must be a matrix (list of lists) of integers/floats"
    if not matrix:
        raise TypeError(errmsg)
    if not isinstance(matrix, list):
        raise TypeError(errmsg)
    for my_list in matrix:
        if not isinstance(my_list, list):
            raise TypeError(errmsg)
        for elem in my_list:
            if not isinstance(elem, int) and not isinstance(elem, float):
                raise TypeError(errmsg)
    for my_list in matrix:
        if len(my_list) == 0:
            raise TypeError(errmsg)
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if not all(len(my_list) == len(matrix[0]) for my_list in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    # round and 2, rounds the result to 2 decimal places
    return [[round(elem / div, 2) for elem in my_list] for my_list in matrix]
