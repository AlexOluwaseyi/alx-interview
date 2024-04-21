#!/usr/bin/python3

def canUnlockAll(boxes):
    n = len(boxes)
    visited = [False] * n

    def dfs(i):
        if visited[i]:
            return

        visited[i] = True
        for key in boxes[i]:
            if 0 <= key < n:
                dfs(key)

    dfs(0)
    return all(visited)
