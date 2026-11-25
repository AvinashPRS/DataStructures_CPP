r"""
    Given preorder traversal data, with null markers, construct the tree.
    Solution:
        In preorder we always go to the left subtree first, then to the right subtree.
        So we keep linking the left child of the current node until we get a null
        marker; then return and do the same for the right child.
        TC: O(n)
        SC: O(h), for recursive stack
"""

# sentinel constant to represent null nodes explicitly
MARKER = -1


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def build_tree_from_preorder_traversal_helper(preorder, index):
    """index: one-element list holding the current position."""
    if index[0] >= len(preorder):
        return None
    current_val = preorder[index[0]]
    index[0] += 1
    if current_val == MARKER:
        return None
    root = Node(current_val)
    root.left = build_tree_from_preorder_traversal_helper(preorder, index)
    root.right = build_tree_from_preorder_traversal_helper(preorder, index)
    return root


def build_tree_from_preorder_traversal(preorder):
    """Builds binary tree from preorder traversal data."""
    return build_tree_from_preorder_traversal_helper(preorder, [0])


def in_order_traversal(node):
    if node:
        in_order_traversal(node.left)
        print(node.data, end=" ")
        in_order_traversal(node.right)


def main():
    r"""
                    1
                  /   \
                2      3
               /  \   /
              4    5  6
                     /
                    7
    """
    preorder = [1, 2, 4, MARKER, MARKER, 5, MARKER, MARKER,
                3, 6, 7, MARKER, MARKER, MARKER, MARKER]
    root = build_tree_from_preorder_traversal(preorder)
    # Expected output order: 4 2 5 1 7 6 3
    in_order_traversal(root)
    print()


if __name__ == "__main__":
    main()
