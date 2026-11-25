"""
Problem: Given a 2D (m X n) matrix with 0 or 1. The aim is to find all regions of 0s which are
enclosed in the matrix, i.e they cannot reach the boundary of the matrix, and make them 1.

NOTE: A node can have edge only with its left, right, up and down neighbour.
Input: 2D matrix
Output: 2D matrix with enclosed 0s flipped to 1s.

Solution:
    We can use the inverse of this problem. It is easier to know the 0s which are touching the
    boundary than the 0s which are not. We start doing BFS from the boundary 0 nodes and mark the
    connected 0 nodes as visited. After that all unvisited 0s comprise the enclosed regions,
    and we mark them as 1.

    TC: O(V + E)
    SC: O(V)

NOTE: the C++ boundary loops mixed up m and n (only correct for square matrices);
this version iterates rows/cols correctly.
"""
from collections import deque

STEPS = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # valid steps


# finds the connected 0-nodes using BFS
def find_nodes_bfs(mat, start, visited):
    m, n = len(mat), len(mat[0])
    q = deque([start])
    visited[start[0]][start[1]] = True  # make the start node visited
    while q:
        cx, cy = q.popleft()
        for dx, dy in STEPS:
            nx, ny = cx + dx, cy + dy
            # coordinates must be valid and the node should be 0
            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and mat[nx][ny] == 0:
                visited[nx][ny] = True
                q.append((nx, ny))


# for finding the enclosed region
def find_enclosed_region(mat):
    m, n = len(mat), len(mat[0])
    visited = [[False] * n for _ in range(m)]

    # start with the boundary 0s
    for j in range(n):  # top and bottom rows
        for i in (0, m - 1):
            if mat[i][j] == 0 and not visited[i][j]:
                find_nodes_bfs(mat, (i, j), visited)
    for i in range(m):  # left and right columns
        for j in (0, n - 1):
            if mat[i][j] == 0 and not visited[i][j]:
                find_nodes_bfs(mat, (i, j), visited)

    # all 0s connected to the boundary 0s have been visited; mark all unvisited 0s as 1
    for i in range(1, m - 1):
        for j in range(1, n - 1):
            if mat[i][j] == 0 and not visited[i][j]:
                mat[i][j] = 1


def print_matrix(mat):
    for row in mat:
        print(" ".join(str(c) for c in row))


# main code harness:
if __name__ == "__main__":
    mat = [
        [0, 0, 1, 1, 1],
        [0, 1, 1, 0, 1],
        [1, 1, 0, 1, 0],
        [1, 0, 0, 1, 1],
        [0, 1, 0, 1, 1],
    ]
    print("BEFORE")
    print_matrix(mat)
    print("\nAFTER")
    find_enclosed_region(mat)
    print_matrix(mat)
