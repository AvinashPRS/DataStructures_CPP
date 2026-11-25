from binary_trees import swap


def binary_tree_size(tree):
    if not tree:
        return 0
    return 1 + binary_tree_size(tree.left) + binary_tree_size(tree.right)


def swap_head(head, node):
    """Detaches the last node and gives it head's children."""
    if node.parent.left is node:
        node.parent.left = None
    else:
        node.parent.right = None
    node.parent = None
    node.left = head.left
    node.right = head.right
    if head.left:
        head.left.parent = node
    if head.right:
        head.right.parent = node
    return head


def perc_down(node):
    """Percolates node down to its correct position. Returns the new head."""
    if not node:
        return None
    nxt = node
    mx = node.n
    if node.left:
        mx = max(node.left.n, mx)
    if node.right:
        mx = max(node.right.n, mx)
    if node.left and mx == node.left.n:
        nxt = node.left
    elif node.right and mx == node.right.n:
        nxt = node.right
    if nxt is not node:
        swap(node, nxt)
        perc_down(node)
    return nxt


def heap_extract(root):
    """Extracts the root node of a Max Binary Heap.

    root: one-element list holding the root. Returns the extracted value
    (0 if the heap is empty).
    """
    if not root or not root[0]:
        return 0
    tmp = root[0]
    size = binary_tree_size(root[0])
    if size == 1:
        res = tmp.n
        root[0] = None
        return res

    # walk to the last node using the binary representation of size
    binary = bin(size)[2:]
    for c in binary[1:]:
        tmp = tmp.right if c == "1" else tmp.left

    head = swap_head(root[0], tmp)
    res = head.n
    root[0] = perc_down(tmp)
    return res
