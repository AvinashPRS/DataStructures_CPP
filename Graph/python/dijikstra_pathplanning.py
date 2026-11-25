"""Dijkstra path planning on a 20x20 occupancy grid (4-connected) with ASCII visualisation."""
import heapq

ROW = 20
COL = 20


def is_valid(r, c):
    return 0 <= r < ROW and 0 <= c < COL


def is_unblocked(grid, r, c):
    return grid[r][c] == 0


def print_visual_grid(grid, path, src, dest):
    display = [['#' if grid[r][c] == 1 else '.' for c in range(COL)] for r in range(ROW)]
    for r, c in path:
        display[r][c] = '*'
    display[src[0]][src[1]] = 'S'
    display[dest[0]][dest[1]] = 'E'

    print("\n================ DIJKSTRA PATH ================\n")
    for r in range(ROW):
        print("  " + "".join(("▒ " if ch == '#' else ch + " ") for ch in display[r]))
    print("\n===============================================")


def trace_path(parent, grid, src, dest):
    path = []
    r, c = dest
    while parent[r][c] != (r, c):
        path.append((r, c))
        r, c = parent[r][c]
    path.append((r, c))
    path.reverse()
    print(f"\nPath coordinates count: {len(path)}")
    print_visual_grid(grid, path, src, dest)


def dijkstra_search(grid, src, dest):
    if not is_valid(*src) or not is_valid(*dest):
        return
    if not is_unblocked(grid, *src) or not is_unblocked(grid, *dest):
        return
    if src == dest:
        return

    visited = [[False] * COL for _ in range(ROW)]
    cost = [[float("inf")] * COL for _ in range(ROW)]
    parent = [[(-1, -1)] * COL for _ in range(ROW)]
    cost[src[0]][src[1]] = 0
    parent[src[0]][src[1]] = src

    pq = [(0, src)]
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while pq:
        _, p = heapq.heappop(pq)
        if visited[p[0]][p[1]]:
            continue
        visited[p[0]][p[1]] = True

        if p == dest:
            print("The destination cell was found via Dijkstra!")
            trace_path(parent, grid, src, dest)
            return

        for dr, dc in moves:
            nr, nc = p[0] + dr, p[1] + dc
            if is_valid(nr, nc) and is_unblocked(grid, nr, nc) and not visited[nr][nc]:
                new_cost = cost[p[0]][p[1]] + 1
                if new_cost < cost[nr][nc]:
                    cost[nr][nc] = new_cost
                    parent[nr][nc] = p
                    heapq.heappush(pq, (new_cost, (nr, nc)))
    print("Failed to find the Destination Cell")


GRID = [
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
]

# main code harness:
if __name__ == "__main__":
    dijkstra_search(GRID, (1, 1), (18, 18))
