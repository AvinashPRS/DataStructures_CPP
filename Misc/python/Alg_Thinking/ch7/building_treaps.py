"""Building Treaps: segment tree for range-max-priority queries."""
import sys

sys.setrecursionlimit(200000)


class SegtreeNode:
    __slots__ = ("left", "right", "max_index")

    def __init__(self):
        self.left = self.right = self.max_index = 0


def init_segtree(segtree, node, left, right):
    segtree[node].left = left
    segtree[node].right = right
    if left == right:
        return
    mid = (left + right) // 2
    init_segtree(segtree, node * 2, left, mid)
    init_segtree(segtree, node * 2 + 1, mid + 1, right)


def fill_segtree(segtree, node, treap_nodes):
    if segtree[node].left == segtree[node].right:
        segtree[node].max_index = segtree[node].left
        return segtree[node].max_index
    left_max = fill_segtree(segtree, node * 2, treap_nodes)
    right_max = fill_segtree(segtree, node * 2 + 1, treap_nodes)
    if treap_nodes[left_max][1] > treap_nodes[right_max][1]:
        segtree[node].max_index = left_max
    else:
        segtree[node].max_index = right_max
    return segtree[node].max_index


def query_segtree(segtree, node, treap_nodes, left, right):
    if right < segtree[node].left or left > segtree[node].right:
        return -1
    if left <= segtree[node].left and segtree[node].right <= right:
        return segtree[node].max_index
    left_max = query_segtree(segtree, node * 2, treap_nodes, left, right)
    right_max = query_segtree(segtree, node * 2 + 1, treap_nodes, left, right)
    if left_max == -1:
        return right_max
    if right_max == -1:
        return left_max
    if treap_nodes[left_max][1] > treap_nodes[right_max][1]:
        return left_max
    return right_max


def solve(treap_nodes, left, right, segtree, out):
    if left > right:
        return
    root_index = query_segtree(segtree, 1, treap_nodes, left, right)
    label, priority = treap_nodes[root_index]
    out.append("(")
    solve(treap_nodes, left, root_index - 1, segtree, out)
    out.append(f"{label}/{priority}")
    solve(treap_nodes, root_index + 1, right, segtree, out)
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
        segtree = [SegtreeNode() for _ in range(num_nodes * 4 + 1)]
        init_segtree(segtree, 1, 0, num_nodes - 1)
        fill_segtree(segtree, 1, treap_nodes)
        solve(treap_nodes, 0, num_nodes - 1, segtree, out)
        print("".join(out))
        num_nodes = int(tokens[pos]) if pos < len(tokens) else 0
        pos += 1


if __name__ == "__main__":
    main()
