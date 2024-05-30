#!/usr/bin/python3

"""
Function to rotate a 2D matrix by 90 degrees
"""


def rotate_2d_matrix(matrix):
    """
    Takes a 2D matrix
    flips it by 90 degree
    Matrix edited in place
    """
    n = len(matrix)
    rez = []
    for i in range(n):
        rez.append([])
        for j in range(n):
            rez[i].append(matrix[j][i])
        rez[i] = reverse_list(rez[i])
    for i in range(n):
        matrix[i] = rez[i]


def reverse_list(lst):
    """Reverse a list in place"""
    n = len(lst)
    for i in range(n // 2):
        lst[i], lst[n - i - 1] = lst[n - i - 1], lst[i]
    return lst
