"""
    Given a binary search tree and two nodes, find the LCA.
    Solution:
        For a binary tree it can be done in O(n). For BST, we can prune the search.
        For a given node:
        1. If the root is either of 'a' or 'b', then it is the LCA.
        2. If 'a' and 'b' lie in opposite subtrees, the root is the LCA.
        3. If the root is lesser than both 'a' and 'b', LCA is in right subtree.
        4. If the root is greater than both 'a' and 'b', LCA is in left subtree.
        TC: worst-case: O(n) skewed tree, Avg. Case: O(h)
        SC: O(h)
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def find_lca_in_bst(root, a, b):
    """Finds the LCA of nodes a and b in a BST."""
    # reached a null node -> no LCA
    if root is None:
        return None
    if root is a or root is b:
        return root
    elif (a.data < root.data < b.data) or (b.data < root.data < a.data):
        return root
    elif root.data < a.data and root.data < b.data:  # both larger
        return find_lca_in_bst(root.right, a, b)
    else:                                            # both smaller
        return find_lca_in_bst(root.left, a, b)


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
    # 8 and 7
    lca = find_lca_in_bst(root, root.right, root.right.left)
    print()
    print(lca.data)


if __name__ == "__main__":
    main()
