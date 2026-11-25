r"""
    Given two tree nodes with parent pointers, find the LCA.
    Solution:
        Take the two pointers to the same depth. Then start traversing
        up the parents till the two are the same node; that is the LCA.
        TC: O(h)
        SC: O(1)
"""


class Node:
    def __init__(self, data, parent=None):
        self.data = data
        self.parent = parent  # non-owning back link
        self.left = None
        self.right = None


def get_depth(node):
    """Finds the depth of a node by climbing parents."""
    depth = 0
    while node and node.parent:
        depth += 1
        node = node.parent
    return depth


def find_lca(node1, node2):
    """Finds the LCA of two nodes."""
    if not node1 or not node2:
        return None
    depth1 = get_depth(node1)
    depth2 = get_depth(node2)
    # climb the deeper node up to the other's depth
    while depth2 > depth1:
        node2 = node2.parent
        depth2 -= 1
    while depth1 > depth2:
        node1 = node1.parent
        depth1 -= 1
    # move both up together until they meet
    while node1 is not node2:
        node1 = node1.parent
        node2 = node2.parent
    return node1


def post_order_traversal(node):
    if node:
        post_order_traversal(node.left)
        post_order_traversal(node.right)
        print(node.data, end=" ")


def main():
    r"""
                     1
                  /    \
                 2      3
                / \    /
               4   5  6
                     /
                    7
    """
    root = Node(1)
    root.left = Node(2, root)
    root.right = Node(3, root)
    root.left.left = Node(4, root.left)
    root.left.right = Node(5, root.left)
    root.right.left = Node(6, root.right)
    root.right.left.left = Node(7, root.right.left)
    post_order_traversal(root)
    print()
    lca = find_lca(root.right.left, root.left.left)
    if lca:
        print("LCA of 6 and 4 is:", lca.data)  # Expected output: 1


if __name__ == "__main__":
    main()
