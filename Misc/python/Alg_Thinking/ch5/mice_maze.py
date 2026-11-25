"""Mice and Maze: one Dijkstra from the exit on the reversed graph."""
import sys


def dijkstra(adj_list, num_cells, from_cell):
    done = [False] * (num_cells + 1)
    min_times = [-1] * (num_cells + 1)
    min_times[from_cell] = 0
    for _ in range(num_cells):
        min_time = -1
        found = False
        for j in range(1, num_cells + 1):
            if not done[j] and min_times[j] >= 0:
                if min_time == -1 or min_times[j] < min_time:
                    min_time = min_times[j]
                    min_time_index = j
                    found = True
        if not found:
            break
        done[min_time_index] = True
        for to_cell, length in adj_list[min_time_index]:
            old_time = min_times[to_cell]
            if old_time == -1 or old_time > min_time + length:
                min_times[to_cell] = min_time + length
    return min_times


def main():
    data = [int(x) for x in sys.stdin.read().split()]
    num_cases = data[0]
    pos = 1
    for case_num in range(1, num_cases + 1):
        num_cells, exit_cell, time_limit, num_edges = data[pos:pos + 4]
        pos += 4
        adj_list = [[] for _ in range(num_cells + 1)]
        for _ in range(num_edges):
            from_cell, to_cell, length = data[pos:pos + 3]
            pos += 3
            adj_list[to_cell].insert(0, (from_cell, length))  # reversed edge
        min_times = dijkstra(adj_list, num_cells, exit_cell)
        total = sum(1 for i in range(1, num_cells + 1)
                    if 0 <= min_times[i] <= time_limit)
        print(total)
        if case_num < num_cases:
            print()


if __name__ == "__main__":
    main()
