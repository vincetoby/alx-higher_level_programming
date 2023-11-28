#!/usr/bin/python3
"""
    a function that multiplies 2 matrices by using
    the module NumPy

    To install it: pip3 install numpy==1.15.0

    Prototype: def lazy_matrix_mul(m_a, m_b):
    Test cases should be the same as 100-matrix_mul
    but with new exception type/message
"""


import numpy as num_num


def lazy_matrix_mul(m_a, m_b):
    """ multiplies two matrix's with numpy """
    return num_num.dot(m_a, m_b)
