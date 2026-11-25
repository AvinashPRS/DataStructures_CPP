"""Two Sum: segment tree storing max element and max pair-sum per range.
Ops: "U x y" sets seq[x] = y; "Q x y" prints the max sum of two
elements in seq[x..y]."""
import sys

sys.setrecursionlimit(100000)


class SegtreeNode:
    __slots__ = ("left", "right", "max_sum", "max_element")

    def __init__(self):
        self.left = self.right = 0
        self.max_sum = self.max_element = -1


def combine(left_info, right_info):
    """Each info is (max_sum, max_element). Returns the merged info."""
    l_sum, l_elem = left_info
    r_sum, r_elem = right_info
    max_element = max(l_elem, r_elem)
    cross = l_elem + r_elem
    if l_sum == -1 and r_sum == -1:
        max_sum = cross
    elif l_sum == -1:
        max_sum = max(cross, r_sum)
    elif r_sum == -1:
        max_sum = max(cross, l_sum)
    else:
        max_sum = max(cross, l_sum, r_sum)
    return max_sum, max_element


def init_segtree(segtree, node, left, right):
    segtree[node].left = left
    segtree[node].right = right
    if left == right:
        return
    mid = (left + right) // 2
    init_segtree(segtree, node * 2, left, mid)
    init_segtree(segtree, node * 2 + 1, mid + 1, right)


def fill_segtree(segtree, node, seq):
    st = segtree[node]
    if st.left == st.right:
        st.max_sum = -1
        st.max_element = seq[st.left]
        return st.max_sum, st.max_element
    left_info = fill_segtree(segtree, node * 2, seq)
    right_info = fill_segtree(segtree, node * 2 + 1, seq)
    st.max_sum, st.max_element = combine(left_info, right_info)
    return st.max_sum, st.max_element


def query_segtree(segtree, node, seq, left, right):
    st = segtree[node]
    if right < st.left or left > st.right:
        return -1, -1
    if left <= st.left and st.right <= right:
        return st.max_sum, st.max_element
    left_info = query_segtree(segtree, node * 2, seq, left, right)
    right_info = query_segtree(segtree, node * 2 + 1, seq, left, right)
    if left_info[1] == -1:
        return right_info
    if right_info[1] == -1:
        return left_info
    return combine(left_info, right_info)


def update_segtree(segtree, node, seq, index):
    st = segtree[node]
    if st.left == st.right:
        st.max_element = seq[index]
        return st.max_sum, st.max_element
    left_node = segtree[node * 2]
    right_node = segtree[node * 2 + 1]
    if index <= left_node.right:
        left_info = update_segtree(segtree, node * 2, seq, index)
        right_info = (right_node.max_sum, right_node.max_element)
    else:
        right_info = update_segtree(segtree, node * 2 + 1, seq, index)
        left_info = (left_node.max_sum, left_node.max_element)
    st.max_sum, st.max_element = combine(left_info, right_info)
    return st.max_sum, st.max_element


def main():
    tokens = sys.stdin.read().split()
    pos = 0
    num_seq = int(tokens[pos])
    pos += 1
    seq = [0] + [int(x) for x in tokens[pos:pos + num_seq]]
    pos += num_seq
    segtree = [SegtreeNode() for _ in range(num_seq * 4 + 1)]
    init_segtree(segtree, 1, 1, num_seq)
    fill_segtree(segtree, 1, seq)
    num_ops = int(tokens[pos])
    pos += 1
    for _ in range(num_ops):
        c, x, y = tokens[pos], int(tokens[pos + 1]), int(tokens[pos + 2])
        pos += 3
        if c == "U":
            seq[x] = y
            update_segtree(segtree, 1, seq, x)
        else:
            print(query_segtree(segtree, 1, seq, x, y)[0])


if __name__ == "__main__":
    main()
