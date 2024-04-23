#!/usr/bin/python3

import sys

"""
a method that determines if all the boxes can be opened.
given n number of lockboxes
using depth-first search
"""

sys.setrecursionlimit(1005)


def canUnlockAll(boxes):
    """
    Function to check if a list of boxes can all be unlocked
    """
    n = len(boxes)
    visited = [False] * n

    def dfs(i):
        """
        Fjnction defition for depth-first search
        """
        if visited[i]:
            return

        visited[i] = True
        for key in boxes[i]:
            if 0 <= key < n:
                dfs(key)

    dfs(0)
    return all(visited)
