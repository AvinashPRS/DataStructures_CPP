"""Feeding Ants: binary search on the amount of liquid poured at the root."""
import sys

sys.setrecursionlimit(10000)

HIGHEST = 2000000000


def can_feed(node, liquid, adj_list, liquid_needed):
    if liquid_needed[node] != -1:
        return liquid >= liquid_needed[node]
    for to_node, percentage, superpipe in adj_list[node]:
        down_pipe = liquid * percentage / 100
        if superpipe:
            down_pipe = down_pipe * down_pipe
        if not can_feed(to_node, down_pipe, adj_list, liquid_needed):
            return False
    return True


def solve(adj_list, liquid_needed):
    low, high = 0.0, float(HIGHEST)
    while high - low > 0.00001:
        mid = (low + high) / 2
        if can_feed(1, mid, adj_list, liquid_needed):
            high = mid
        else:
            low = mid
    print(f"{high:.4f}")


def main():
    data = [int(x) for x in sys.stdin.read().split()]
    num_nodes = data[0]
    pos = 1
    adj_list = [[] for _ in range(num_nodes + 1)]
    for _ in range(num_nodes - 1):
        from_node, to_node, percentage, superpipe = data[pos:pos + 4]
        pos += 4
        adj_list[from_node].insert(0, (to_node, percentage, superpipe))
    liquid_needed = [0] + data[pos:pos + num_nodes]
    solve(adj_list, liquid_needed)


if __name__ == "__main__":
    main()
