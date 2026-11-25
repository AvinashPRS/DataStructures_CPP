"""Drawer Chore (Ladice): union-find where set 0 means 'full'."""
import sys


def find(x, parent):
    """Find with path compression."""
    root = x
    while parent[root] != root:
        root = parent[root]
    while parent[x] != root:
        parent[x], x = root, parent[x]
    return root


def union_sets(drawer1, drawer2, parent):
    set1 = find(drawer1, parent)
    set2 = find(drawer2, parent)
    parent[set1] = set2
    if set1 == set2:
        parent[set2] = 0
    print("LADICA")


def main():
    data = [int(x) for x in sys.stdin.read().split()]
    num_items, num_drawers = data[0], data[1]
    parent = list(range(num_drawers + 1))
    pos = 2
    for _ in range(num_items):
        drawer_a, drawer_b = data[pos], data[pos + 1]
        pos += 2
        if find(drawer_a, parent) == drawer_a:
            union_sets(drawer_a, drawer_b, parent)
        elif find(drawer_b, parent) == drawer_b:
            union_sets(drawer_b, drawer_a, parent)
        elif find(drawer_a, parent) > 0:
            union_sets(drawer_a, drawer_b, parent)
        elif find(drawer_b, parent) > 0:
            union_sets(drawer_b, drawer_a, parent)
        else:
            print("SMECE")


if __name__ == "__main__":
    main()
