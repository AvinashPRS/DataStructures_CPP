"""
Problem: Given a 2D maze of Black and white tiles and a starting and destination tile. White
tiles are accessible and black ones are not. Check if there exists a path from the starting tile
to the destination tile. We can only move forward, backward, left and right.
Input: 2D matrix
Output: bool (and the path)

Solution: We can use either BFS or DFS for this.
TC: O(V + E)
SC: O(V)
"""
from collections import deque

WHITE, BLACK = 0, 1  # tile colors

# valid steps: neighbouring nodes in 4 directions excluding the diagonals
STEPS = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def is_valid_step(maze, step):
    # a step is valid if it is within the maze boundary and it is a white tile
    x, y = step
    return 0 <= x < len(maze) and 0 <= y < len(maze[x]) and maze[x][y] == WHITE


def search_bfs(maze, start, dest):
    """BFS; to recover the path we keep a queue of paths alongside the queue of nodes.
    Returns the shortest path (list of coordinates) or None."""
    q = deque([(start, [start])])
    maze[start[0]][start[1]] = BLACK  # make it BLACK (visited)
    while q:
        curr, curr_path = q.popleft()
        if curr == dest:
            return curr_path
        for dx, dy in STEPS:
            nxt = (curr[0] + dx, curr[1] + dy)
            if is_valid_step(maze, nxt):
                maze[nxt[0]][nxt[1]] = BLACK
                q.append((nxt, curr_path + [nxt]))
    return None


def search_dfs(maze, curr, dest, path):
    """DFS; `path` is extended in place. Returns True if dest was reached."""
    if curr == dest:
        return True
    for dx, dy in STEPS:
        nxt = (curr[0] + dx, curr[1] + dy)
        if is_valid_step(maze, nxt):
            # make it black and add to path
            maze[nxt[0]][nxt[1]] = BLACK
            path.append(nxt)
            if search_dfs(maze, nxt, dest, path):
                return True
            # if there is no possible path, then remove the current node
            path.pop()
    return False


def maze_search(maze, start, dest):
    """Driver: returns the path from start to dest (empty list if none). Uses BFS."""
    path = search_bfs(maze, start, dest)
    if path is not None:
        return path
    maze[start[0]][start[1]] = WHITE
    return []


def print_maze(maze):
    for row in maze:
        print(" ".join(str(c) for c in row))


def print_path(path):
    if path:
        print("PATH: ")
        print(" ".join(f"{{{x}, {y}}}" for x, y in path))
    else:
        print("There is no path for the starting and dest coordinates.")


# main code harness:
if __name__ == "__main__":
    maze = [
        [0, 0, 1, 0, 1],
        [0, 0, 0, 0, 0],
        [1, 0, 0, 1, 0],
        [1, 0, 0, 1, 1],
        [0, 1, 0, 0, 0],
    ]
    start, dest = (0, 0), (4, 4)
    print_maze(maze)
    dfs_maze = [row[:] for row in maze]
    print_path(maze_search(maze, start, dest))

    # DFS variant (not necessarily shortest)
    dfs_maze[start[0]][start[1]] = BLACK
    p = [start]
    print("DFS", end=" ")
    print_path(p if search_dfs(dfs_maze, start, dest, p) else [])
