"""
    Given a BST and a key, find the first node whose data value is greater than the key.
    Solution:
        Do normal BST search; whenever we see a node > key remember it and go left,
        otherwise go right.
        TC: O(h)
        SC: O(1)
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def find_just_greater_node(root, key):
    """Finds the node with the smallest value greater than key."""
    just_greater = None  # last seen greater node
    curr = root
    while curr:
        if curr.data > key:
            just_greater = curr
            curr = curr.left
        else:
            curr = curr.right
    return just_greater


def in_order_traversal(node):
    if node:
        in_order_traversal(node.left)
        print(node.data, end=" ")
        in_order_traversal(node.right)


def build_sample_bst():
    r"""
                    5
                  /   \
                2      8
               /  \   /  \
              1    3  7   9
                     /
                    6
    """
    root = Node(5)
    root.left = Node(2)
    root.right = Node(8)
    root.left.left = Node(1)
    root.left.right = Node(3)
    root.right.left = Node(7)
    root.right.left.left = Node(6)
    root.right.right = Node(9)
    return root


def main():
    root = build_sample_bst()
    in_order_traversal(root)
    print()
    print(find_just_greater_node(root, 2).data)


if __name__ == "__main__":
    main()
