"""
    Given traversal orders in inorder and preorder. Construct a binary tree from this traversal data.
    Solution:
        Preorder always gives the root of a tree first and inorder first traverses the left,
        current root and right subtree. So the first element of preorder is the root; we find
        the root in inorder, the nodes on its left form the left subtree and nodes on its
        right form the right subtree.
        A hash table mapping node data -> inorder index makes root lookup O(1).
        TC: O(n)
        SC: O(h + n), for recursive stack + hash table
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def build_tree_from_traversal_helper(inorder, inorder_s, inorder_e,
                                     preorder, preorder_s, preorder_e,
                                     inorder_mapping):
    if preorder_s > preorder_e or inorder_s > inorder_e:
        return None
    root_data = preorder[preorder_s]
    root_idx = inorder_mapping[root_data]
    num_nodes_left = root_idx - inorder_s

    root = Node(root_data)
    root.left = build_tree_from_traversal_helper(
        inorder, inorder_s, root_idx - 1,
        preorder, preorder_s + 1, preorder_s + num_nodes_left,
        inorder_mapping)
    root.right = build_tree_from_traversal_helper(
        inorder, root_idx + 1, inorder_e,
        preorder, preorder_s + num_nodes_left + 1, preorder_e,
        inorder_mapping)
    return root


def build_tree_from_traversal(inorder, preorder):
    """Builds binary tree from inorder and preorder traversal data."""
    inorder_mapping = {val: i for i, val in enumerate(inorder)}
    return build_tree_from_traversal_helper(inorder, 0, len(inorder) - 1,
                                            preorder, 0, len(preorder) - 1,
                                            inorder_mapping)


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
    inorder = [4, 2, 5, 1, 7, 6, 3]
    preorder = [1, 2, 4, 5, 3, 6, 7]
    root = build_tree_from_traversal(inorder, preorder)
    in_order_traversal(root)
    print()


if __name__ == "__main__":
    main()
