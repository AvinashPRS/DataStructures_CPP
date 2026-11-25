"""
    Check if a tree is height balanced or not.
    Tree is height balanced if the height diff between left and right subtree is
    max 1.
    Solution:
        We do a postorder traversal and while going up check for the
        height diff of each descendant subtree. If the diff is more than 1,
        return false.
        TC: O(n)
        SC: O(h), for recursive stack
"""
from collections import namedtuple

HeightInfo = namedtuple("HeightInfo", ["balanced", "height"])


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def check_height_balanced(root):
    if root is None:
        return HeightInfo(True, -1)
    left = check_height_balanced(root.left)
    if not left.balanced:
        return HeightInfo(False, 0)
    right = check_height_balanced(root.right)
    if not right.balanced:
        return HeightInfo(False, 0)
    is_balanced = abs(left.height - right.height) <= 1
    parent_height = max(left.height, right.height) + 1
    return HeightInfo(is_balanced, parent_height)


def is_height_balanced(root):
    """Checks if the tree is height balanced or not."""
    return check_height_balanced(root).balanced


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
    print(int(is_height_balanced(root)))


if __name__ == "__main__":
    main()
