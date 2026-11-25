"""A Python program to implement A* Search Algorithm (8-connected grid, Euclidean heuristic)."""
import heapq
import math

ROW = 9
COL = 10
FLT_MAX = float("inf")

# 8 successors of a cell, in the same order as the C++ version:
#   N, S, E, W, N.E, N.W, S.E, S.W   (straight moves cost 1.0, diagonals 1.414)
#
#       N.W  N  N.E
#          \ | /
#     W----Cell----E
#          / | \
#       S.W  S  S.E
SUCCESSORS = [
    (-1, 0, 1.0), (1, 0, 1.0), (0, 1, 1.0), (0, -1, 1.0),
    (-1, 1, 1.414), (-1, -1, 1.414), (1, 1, 1.414), (1, -1, 1.414),
]


class Cell:
    """Necessary parameters per cell. f = g + h."""
    __slots__ = ("parent_i", "parent_j", "f", "g", "h")

    def __init__(self):
        self.parent_i = -1  # Row and Column index of its parent
        self.parent_j = -1
        self.f = FLT_MAX
        self.g = FLT_MAX
        self.h = FLT_MAX


def is_valid(row, col):
    """Is (row, col) inside the grid?"""
    return 0 <= row < ROW and 0 <= col < COL


def is_unblocked(grid, row, col):
    """True if the cell is not blocked (1 = free in this file)."""
    return grid[row][col] == 1


def is_destination(row, col, dest):
    return (row, col) == dest


def calculate_h_value(row, col, dest):
    """'h' heuristic: Euclidean distance."""
    return math.sqrt((row - dest[0]) ** 2 + (col - dest[1]) ** 2)


def trace_path(cell_details, dest):
    """Trace the path from the source to destination."""
    print("\nThe Path is ", end="")
    row, col = dest
    path = []
    while not (cell_details[row][col].parent_i == row and cell_details[row][col].parent_j == col):
        path.append((row, col))
        row, col = cell_details[row][col].parent_i, cell_details[row][col].parent_j
    path.append((row, col))
    for r, c in reversed(path):
        print(f"-> ({r},{c}) ", end="")


def a_star_search(grid, src, dest):
    """Find the shortest path between src and dest according to A* Search."""
    if not is_valid(*src):
        print("Source is invalid")
        return
    if not is_valid(*dest):
        print("Destination is invalid")
        return
    if not is_unblocked(grid, *src) or not is_unblocked(grid, *dest):
        print("Source or the destination is blocked")
        return
    if is_destination(src[0], src[1], dest):
        print("We are already at the destination")
        return

    # closed list: no cell has been included yet
    closed_list = [[False] * COL for _ in range(ROW)]
    cell_details = [[Cell() for _ in range(COL)] for _ in range(ROW)]

    # Initialising the parameters of the starting node
    i, j = src
    start = cell_details[i][j]
    start.f = start.g = start.h = 0.0
    start.parent_i, start.parent_j = i, j

    # Open list of (f, i, j). The C++ version uses std::set<pair<double, pair<int,int>>>;
    # a heap of the same tuples pops elements in the same order.
    open_list = [(0.0, i, j)]

    while open_list:
        _, i, j = heapq.heappop(open_list)
        closed_list[i][j] = True  # Add this vertex to the closed list

        for di, dj, step_cost in SUCCESSORS:
            ni, nj = i + di, j + dj
            # Only process this cell if this is a valid one
            if not is_valid(ni, nj):
                continue
            # If the destination cell is the same as the current successor
            if is_destination(ni, nj, dest):
                cell_details[ni][nj].parent_i = i
                cell_details[ni][nj].parent_j = j
                print("The destination cell is found")
                trace_path(cell_details, dest)
                return
            # If the successor is already on the closed list or is blocked, ignore it.
            if not closed_list[ni][nj] and is_unblocked(grid, ni, nj):
                g_new = cell_details[i][j].g + step_cost
                h_new = calculate_h_value(ni, nj, dest)
                f_new = g_new + h_new
                # If it isn't on the open list, add it. Make the current square the parent and
                # record f, g and h.  OR  if it is on the open list already, check whether this
                # path is better, using 'f' cost as the measure.
                cd = cell_details[ni][nj]
                if cd.f == FLT_MAX or cd.f > f_new:
                    heapq.heappush(open_list, (f_new, ni, nj))
                    cd.f, cd.g, cd.h = f_new, g_new, h_new
                    cd.parent_i, cd.parent_j = i, j

    # open list is empty and we never reached the destination (e.g. due to blockages)
    print("Failed to find the Destination Cell")


# Driver program to test above function
if __name__ == "__main__":
    # Description of the Grid - 1: the cell is not blocked, 0: the cell is blocked
    grid = [
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 0, 1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
        [0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
        [1, 0, 1, 1, 1, 1, 0, 1, 0, 0],
        [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 0, 0, 0, 1, 0, 0, 1],
    ]
    src = (8, 0)   # left-most bottom-most corner
    dest = (0, 0)  # left-most top-most corner
    a_star_search(grid, src, dest)
    print()
