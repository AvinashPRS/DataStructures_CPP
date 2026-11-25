"""Building Treaps - too slow (uses linear search for max priority)."""
import sys

sys.setrecursionlimit(200000)


def max_priority_index(treap_nodes, left, right):
    max_index = left
    for i in range(left + 1, right + 1):
        if treap_nodes[i][1] > treap_nodes[max_index][1]:
            max_index = i
    return max_index


def solve(treap_nodes, left, right, out):
    if left > right:
        return
    root_index = max_priority_index(treap_nodes, left, right)
    label, priority = treap_nodes[root_index]
    out.append("(")
    solve(treap_nodes, left, root_index - 1, out)
    out.append(f"{label}/{priority}")
    solve(treap_nodes, root_index + 1, right, out)
    out.append(")")


def main():
    tokens = sys.stdin.read().split()
    pos = 0
    num_nodes = int(tokens[pos])
    pos += 1
    while num_nodes > 0:
        treap_nodes = []
        for _ in range(num_nodes):
            label, priority = tokens[pos].rsplit("/", 1)
            pos += 1
            treap_nodes.append((label, int(priority)))
        treap_nodes.sort(key=lambda t: t[0])
        out = []
        solve(treap_nodes, 0, num_nodes - 1, out)
        print("".join(out))
        num_nodes = int(tokens[pos]) if pos < len(tokens) else 0
        pos += 1


if __name__ == "__main__":
    main()
