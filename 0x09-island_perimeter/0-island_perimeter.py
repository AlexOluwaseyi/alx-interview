#!/usr/bin/python3

"""
For the “0. Island Perimeter” project, you will need to apply your
knowledge of algorithms, data structures (specifically matrices or
2D lists), and iterative or conditional logic to solve a geometric
problem within a grid context. The goal is to calculate the perimeter
of a single island in a grid, where the grid is represented by a 2D
array of integers. Understanding how to navigate and analyze 2D arrays
and apply logical operations to determine the conditions for perimeter
calculation is crucial for this task.
"""


def island_perimeter(grid):
    """
    A function def island_perimeter(grid): that returns
    the perimeter of the island described in grid:
    - grid is a list of list of integers:
      - 0 represents water
      - 1 represents land
      - Each cell is square, with a side length of 1
      - Cells are connected horizontally/vertically (not diagonally).
      - grid is rectangular, with its width and height not exceeding 100
    - The grid is completely surrounded by water
    - There is only one island (or nothing).
    - The island doesn’t have “lakes” (water inside that isn't
      connected to the water surrounding the island).
    """
    n = len(grid)
    perimeter = 0
    for row in range(n):
        for col in range(len(grid[row])):
            if grid[row][col] == 1:
                perimeter += 4
                if 0 <= row - 1 < row and grid[row - 1][col] == 1:
                    perimeter -= 2
                if 0 <= col - 1 < col and grid[row][col - 1] == 1:
                    perimeter -= 2

    return perimeter
