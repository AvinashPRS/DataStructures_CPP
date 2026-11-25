"""
    Given a binary tree and a tree node. Find the inorder successor of
    the node.
    Solution:
        In inorder traversal, we first go to left subtree, current and then
        right subtree. So for the given node, if the right subtree is present
        then the successor is the leftmost node in that subtree.
        If the right subtree is not present, then the inorder successor
        is the first ancestor whose left subtree contains this node.
        TC: O(h)
        SC: O(1)
"""


class Node:
    def __init__(self, data, parent=None):
        self.data = data
        self.parent = parent
        self.left = None
        self.right = None


def find_successor(root, node):
    """Finds the inorder successor of a given node."""
    if node.right is not None:
        # left most node of the right subtree
        curr = node.right
        while curr.left:
            curr = curr.left
        return curr
    # climb up until current is part of a left subtree
    curr = node
    while curr.parent and curr is not curr.parent.left:
        curr = curr.parent
    return curr.parent


def in_order_traversal(node):
    if node:
        in_order_traversal(node.left)
        print(node.data, end=" ")
        in_order_traversal(node.right)


def build_sample_tree():
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
    return root


def main():
    root = build_sample_tree()
    in_order_traversal(root)
    print()
    result = find_successor(root, root.right)
    if result:
        print(result.data)
    else:
        print("No successor")


if __name__ == "__main__":
    main()
