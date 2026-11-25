"""
Problem: Given a 2D matrix of m X n. The tiles are colored either black or white. Given a
position (x, y) flip the color of the entire region connected to that point. The region
consists of all points reachable from that point having the same color.
We can only move forward, backward, left and right.

Solution: BFS or DFS from the given point, flipping colours of same-coloured neighbours.

TC: O(mn)
SC: O(m+n)
"""
from collections import deque

# possible relative neighbor coordinates (row, col) - any order is possible
STEPS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
WHITE, BLACK = 0, 1


def is_valid(arr, x, y):
    # step should lie within bounds of Matrix
    return 0 <= x < len(arr) and 0 <= y < len(arr[0])


# flipping the colors using DFS (in place)
def flip_color_dfs(arr, curr):
    x, y = curr
    color = arr[x][y]       # color to flip
    arr[x][y] = 1 - color   # flip the color of current tile
    for dx, dy in STEPS:
        nx, ny = x + dx, y + dy
        # if the adjacent node is of same color and is a valid position
        if is_valid(arr, nx, ny) and arr[nx][ny] == color:
            flip_color_dfs(arr, (nx, ny))


# color flipping using BFS (returns a new matrix)
def flip_color_bfs(arr, start):
    arr = [row[:] for row in arr]
    color = arr[start[0]][start[1]]
    # NOTE: the C++ version never flips the start pixel itself (it only flips neighbours);
    # we flip it here so BFS and DFS produce identical results.
    arr[start[0]][start[1]] = 1 - color
    q = deque([start])
    while q:
        x, y = q.popleft()
        for dx, dy in STEPS:
            nx, ny = x + dx, y + dy
            if is_valid(arr, nx, ny) and arr[nx][ny] == color:
                arr[nx][ny] = 1 - color  # flip and enqueue
                q.append((nx, ny))
    return arr


def print_matrix(arr):
    for row in arr:
        print(" ".join(str(p) for p in row))


if __name__ == "__main__":
    arr = [
        [0, 0, 1, 0, 1],
        [0, 0, 0, 0, 0],
        [1, 0, 0, 1, 0],
        [1, 0, 0, 1, 1],
        [0, 1, 0, 0, 0],
    ]
    print("BEFORE:")
    print_matrix(arr)
    print("\nBFS")
    print_matrix(flip_color_bfs(arr, (4, 4)))
    print("\nDFS")
    flip_color_dfs(arr, (4, 4))
    print_matrix(arr)
