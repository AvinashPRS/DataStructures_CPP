"""
Problem: Given a 2D maze of black and white tiles plus a start and a
destination tile, check whether there is a path from start to destination.
White tiles are accessible, black ones are not. Moves: up/down/left/right.

Solution: BFS (gives the shortest path) or DFS.
    TC: O(V + E)
    SC: O(V)
"""
from collections import deque

WHITE, BLACK = 0, 1

# neighbours: the 4 adjacent tiles (no diagonals)
STEPS = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def is_valid_step(maze, step):
    """Inside the maze boundary and a white tile."""
    x, y = step
    return 0 <= x < len(maze) and 0 <= y < len(maze[x]) and maze[x][y] == WHITE


def search_bfs(maze, start, dest):
    """Returns the shortest path as a list of coordinates, or None.
    Visited tiles are marked BLACK."""
    q = deque([(start, [start])])  # (node, path to node)
    maze[start[0]][start[1]] = BLACK
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
    """Appends the path to `path`; returns True if dest is reachable."""
    if curr == dest:
        return True
    for dx, dy in STEPS:
        nxt = (curr[0] + dx, curr[1] + dy)
        if is_valid_step(maze, nxt):
            maze[nxt[0]][nxt[1]] = BLACK
            path.append(nxt)
            if search_dfs(maze, nxt, dest, path):
                return True
            path.pop()  # dead end: remove the node
    return False


def maze_search(maze, start, dest):
    # visited nodes are tracked by turning them BLACK
    maze[start[0]][start[1]] = BLACK
    path = search_bfs(maze, start, dest)
    if path:
        return path
    maze[start[0]][start[1]] = WHITE
    return []


def print_maze(maze):
    for row in maze:
        print("".join(f"{c} " for c in row))


def print_path(path):
    if path:
        print("PATH: ")
        print("".join(f"{{{x}, {y}}} " for x, y in path))
    else:
        print("There is no path for the starting and dest coordinates.")


def main():
    maze = [[0, 0, 1, 0, 1],
            [0, 0, 0, 0, 0],
            [1, 0, 0, 1, 0],
            [1, 0, 0, 1, 1],
            [0, 1, 0, 0, 0]]
    start, dest = (0, 0), (4, 4)
    print_maze(maze)
    print_path(maze_search(maze, start, dest))


if __name__ == "__main__":
    main()
