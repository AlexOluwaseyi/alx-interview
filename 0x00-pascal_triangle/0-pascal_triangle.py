#!/usr/bin/python3

"""
Python module to generate a Pascal triangle
"""


def pascal_triangle(n):
    """
    Function pascal_triangle to generate n number of rows of pascal triangle
    """
    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        if i >= 2:
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    return triangle
