"""
    Given a binary tree where the nodes have parent link. Implement
    inorder traversal with O(1) space.
    Solution:
        Main problem is to not print a node twice. This depends on how we reach
        a node, whether from its parent, its left or its right subtree.
        1. Going down: go left if possible, else print and go right / up
        2. Going up from left: print current, go right if possible, else up
        3. Going up from right: go up
        TC: O(n)
        SC: O(1)
"""


class Node:
    def __init__(self, data, parent=None):
        self.data = data
        self.parent = parent
        self.left = None
        self.right = None


def in_order_traversal_constant_space(root):
    """Inorder traversal with constant space (uses parent links)."""
    if root is None:
        return
    curr, prev = root, None
    while curr is not None:
        if prev is curr.parent:              # going down the tree
            if curr.left:
                nxt = curr.left
            else:
                print(curr.data, end=" ")
                nxt = curr.right if curr.right else curr.parent
        elif curr.left is prev:              # coming up from the left
            print(curr.data, end=" ")
            nxt = curr.right if curr.right else curr.parent
        else:                                # coming up from the right
            nxt = curr.parent
        prev, curr = curr, nxt


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
    in_order_traversal_constant_space(root)
    print()


if __name__ == "__main__":
    main()
