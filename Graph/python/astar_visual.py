"""A* search on a 9x10 grid (4-connected, Manhattan heuristic) with ASCII visualisation."""
import heapq

ROW = 9
COL = 10
INF = float("inf")


def is_valid(r, c):
    return 0 <= r < ROW and 0 <= c < COL


def is_unblocked(grid, r, c):
    return grid[r][c] == 0


def calculate_h_value(r, c, dest):
    """Manhattan distance heuristic."""
    return abs(r - dest[0]) + abs(c - dest[1])


def print_visual_grid(grid, path, src, dest):
    """Visually maps out and prints the grid with the path drawn on it."""
    display = [['#' if grid[r][c] == 1 else '.' for c in range(COL)] for r in range(ROW)]
    for r, c in path:          # overlay the calculated path
        display[r][c] = '*'
    display[src[0]][src[1]] = 'S'   # explicit start and end symbols
    display[dest[0]][dest[1]] = 'E'

    print("\n================ VISUAL PATH ================\n")
    for r in range(ROW):
        print("  " + "".join(("▒ " if ch == '#' else ch + " ") for ch in display[r]))
    print("\n=============================================")


def trace_path(parent, grid, src, dest):
    """Trace the final path from destination to source using parent pointers.
    The source cell was configured to point to itself as its own parent."""
    r, c = dest
    path = []
    while parent[r][c] != (r, c):
        path.append((r, c))
        r, c = parent[r][c]
    path.append((r, c))
    path.reverse()
    print("\nPath coordinates: " + " -> ".join(f"({r},{c})" for r, c in path))
    print_visual_grid(grid, path, src, dest)


def a_star_search(grid, src, dest):
    if not is_valid(*src) or not is_valid(*dest):
        return
    if not is_unblocked(grid, *src) or not is_unblocked(grid, *dest):
        return
    if src == dest:
        return

    closed_list = [[False] * COL for _ in range(ROW)]
    f = [[INF] * COL for _ in range(ROW)]
    g = [[INF] * COL for _ in range(ROW)]
    parent = [[(-1, -1)] * COL for _ in range(ROW)]

    r, c = src
    f[r][c] = g[r][c] = 0
    parent[r][c] = (r, c)  # point to itself as its own parent

    open_list = [(0, src)]  # min heap of (f, (r, c))
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while open_list:
        _, (r, c) = heapq.heappop(open_list)
        closed_list[r][c] = True

        for dr, dc in moves:
            nr, nc = r + dr, c + dc
            if not is_valid(nr, nc):
                continue
            # reached destination:
            if (nr, nc) == dest:
                parent[nr][nc] = (r, c)
                print("The destination cell was found!")
                trace_path(parent, grid, src, dest)
                return
            elif not closed_list[nr][nc] and is_unblocked(grid, nr, nc):
                g_new = g[r][c] + 1
                f_new = g_new + calculate_h_value(nr, nc, dest)
                if f[nr][nc] == INF or f[nr][nc] > f_new:
                    heapq.heappush(open_list, (f_new, (nr, nc)))
                    f[nr][nc] = f_new
                    g[nr][nc] = g_new
                    parent[nr][nc] = (r, c)
    print("Failed to find the Destination Cell")


# 0 = Walkable, 1 = ▒ Obstacle Block
GRID = [
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 1, 1, 0],
    [0, 0, 1, 1, 1, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 1, 1, 1, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

# main code harness:
if __name__ == "__main__":
    a_star_search(GRID, (0, 0), (8, 9))
