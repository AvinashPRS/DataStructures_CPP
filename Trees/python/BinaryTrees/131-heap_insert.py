from binary_trees import BinaryTreeNode


def swap(a, b):
    """Swaps node a with its child b in the tree. Returns the tree root."""
    a_parent, a_left, a_right = a.parent, a.left, a.right

    a.parent = b
    a.left = b.left
    a.right = b.right
    if b.left:
        b.left.parent = a
    if b.right:
        b.right.parent = a

    b.parent = a_parent
    if a_parent:
        if a is a_parent.left:
            a_parent.left = b
        else:
            a_parent.right = b

    if b is a_left:
        b.left = a
        b.right = a_right
        if a_right:
            a_right.parent = b
    elif b is a_right:
        b.right = a
        b.left = a_left
        if a_left:
            a_left.parent = b

    while b.parent:
        b = b.parent
    return b


def convert(num, base, lowercase=1):
    """Converts a number to a string in the given base."""
    rep = "0123456789abcdef" if lowercase else "0123456789ABCDEF"
    out = ""
    while True:
        out = rep[num % base] + out
        num //= base
        if not num:
            break
    return out


def binary_tree_size(tree):
    if not tree:
        return 0
    return 1 + binary_tree_size(tree.left) + binary_tree_size(tree.right)


def insert(root, node):
    """Places node at the next free position of the complete tree.
    The binary representation of (size + 1), minus its leading 1, is the
    path from the root: 0 = left, 1 = right."""
    tmp = root[0]
    binary = convert(binary_tree_size(tmp) + 1, 2, 1)
    for i in range(1, len(binary)):
        c = binary[i]
        if i == len(binary) - 1:
            node.parent = tmp
            if c == "1":
                tmp.right = node
            else:
                tmp.left = node
            break
        tmp = tmp.right if c == "1" else tmp.left


def heap_insert(root, value):
    """Inserts value in a Max Binary Heap.

    root: one-element list holding the root. Returns the created node.
    """
    if root is None:
        return None
    ht = BinaryTreeNode(value)
    if root[0] is None:
        root[0] = ht
        return ht
    insert(root, ht)
    while ht.parent and ht.n > ht.parent.n:
        ret = swap(ht.parent, ht)
        if ret:
            root[0] = ret
    return ht
