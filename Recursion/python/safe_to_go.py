"""
Question -> Source to Destination allowed only two moves Right or UP.
Print every path from source to destination inside an m x n matrix.
"""

visited = set()


def safe_to_go(a, b, m, n):
    """Point should be a new point and it should be inside the matrix boundary."""
    return 0 <= a < m and 0 <= b < n and (a, b) not in visited


def print_ways(m, n, src_x, src_y, dest_x, dest_y, output):
    visited.add((src_x, src_y))

    # base Condition
    if src_x == dest_x and src_y == dest_y:
        print(f"ANSWER -> {''.join(output)}")
        visited.discard((src_x, src_y))
        return

    # RIGHT
    if safe_to_go(src_x + 1, src_y, m, n):
        output.append("R")
        print_ways(m, n, src_x + 1, src_y, dest_x, dest_y, output)
        output.pop()  # backtracking

    # UP
    if safe_to_go(src_x, src_y + 1, m, n):
        output.append("U")
        print_ways(m, n, src_x, src_y + 1, dest_x, dest_y, output)
        output.pop()  # backtracking

    # if we add this line, we get overlapping paths and if we dont add this, we get independent paths
    visited.discard((src_x, src_y))


if __name__ == "__main__":
    m, n = 3, 3  # Matrix boundaries
    src_x, src_y = 0, 0
    dest_x, dest_y = 2, 2

    print("Ways to reach from Origin to Destination are as follows:")
    # 'output' is a list used as a mutable string so backtracking avoids copies
    print_ways(m, n, src_x, src_y, dest_x, dest_y, [])
