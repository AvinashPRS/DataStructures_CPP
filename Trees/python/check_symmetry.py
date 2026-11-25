"""
    Check if tree is symmetric about root.
    Solution:
        Start simultaneous traversal of left and right subtrees, if the
        tree is symmetric, then the left and right subtree values will always
        be equal.
        TC: O(n)
        SC: O(h), for recursive stack
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def check_tree_symmetry(node1, node2):
    # both null
    if node1 is None and node2 is None:
        return True
    # only one of them is null -> symmetry breaks
    if node1 is None or node2 is None:
        return False
    return (node1.data == node2.data and
            check_tree_symmetry(node1.left, node2.right) and
            check_tree_symmetry(node1.right, node2.left))


def is_symmetric(root):
    """Checks if the given tree is symmetric about root."""
    return check_tree_symmetry(root.left, root.right)


def post_order_traversal(node):
    if node:
        post_order_traversal(node.left)
        post_order_traversal(node.right)
        print(node.data, end=" ")


def build_sample_tree():
    r"""
                    1
                  /   \
                2      3
               /  \   /
              4    5  6
                     /
                    7
    """
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.left.left = Node(7)
    return root


def main():
    root = build_sample_tree()
    post_order_traversal(root)
    print()
    print(int(is_symmetric(root)))


if __name__ == "__main__":
    main()
