"""Food Lines: each new person joins the shortest line."""
import sys


def shortest_line_index(lines):
    shortest = 0
    for j in range(1, len(lines)):
        if lines[j] < lines[shortest]:
            shortest = j
    return shortest


def solve(lines, m):
    for _ in range(m):
        shortest = shortest_line_index(lines)
        print(lines[shortest])
        lines[shortest] += 1


def main():
    data = sys.stdin.read().split()
    n, m = int(data[0]), int(data[1])
    lines = [int(x) for x in data[2:2 + n]]
    solve(lines, m)


if __name__ == "__main__":
    main()
