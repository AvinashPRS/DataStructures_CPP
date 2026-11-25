r"""
    Given a preorder or postorder traversal sequence of a BST, construct the BST from it.
    Solution:
        We build the tree incrementally, keeping an index of the current element.
        For preorder:
            Each element is a root. With each recursion call we send the range in which
            its child can exist; if the next element is in that range we add it as the
            child, otherwise the child is NULL and we go back up.
        For postorder:
            Same concept, but the root is visited last, so we start from the back of the
            sequence and build the right subtree before the left subtree.
        TC: O(n)
        SC: O(n) for n elements

                    5
                  /   \
                2      8
               /  \   /  \
              1    3  7   9
                     /
                    6
"""

INT_MIN, INT_MAX = -2 ** 31, 2 ** 31 - 1


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def build_bst_from_preorder_helper(preorder, curr_idx, lower_limit, upper_limit):
    """curr_idx: one-element list holding the current index."""
    if curr_idx[0] >= len(preorder):
        return None
    key = preorder[curr_idx[0]]
    if key < lower_limit or key > upper_limit:
        return None
    root = Node(key)
    curr_idx[0] += 1
    root.left = build_bst_from_preorder_helper(preorder, curr_idx, lower_limit, key - 1)
    root.right = build_bst_from_preorder_helper(preorder, curr_idx, key + 1, upper_limit)
    return root


def build_bst_from_preorder(preorder):
    """Creates BST from preorder traversal sequence."""
    return build_bst_from_preorder_helper(preorder, [0], INT_MIN, INT_MAX)


def build_bst_from_postorder_helper(postorder, curr_idx, lower_limit, upper_limit):
    if curr_idx[0] < 0:
        return None
    key = postorder[curr_idx[0]]
    if key < lower_limit or key > upper_limit:
        return None
    root = Node(key)
    curr_idx[0] -= 1
    # right subtree first, then left
    root.right = build_bst_from_postorder_helper(postorder, curr_idx, key + 1, upper_limit)
    root.left = build_bst_from_postorder_helper(postorder, curr_idx, lower_limit, key - 1)
    return root


def build_bst_from_postorder(postorder):
    """Creates BST from postorder traversal sequence."""
    return build_bst_from_postorder_helper(postorder, [len(postorder) - 1], INT_MIN, INT_MAX)


def in_order_traversal(node):
    if node:
        in_order_traversal(node.left)
        print(node.data, end=" ")
        in_order_traversal(node.right)


def main():
    preorder = [5, 2, 1, 3, 8, 7, 6, 9]
    postorder = [1, 3, 2, 6, 7, 9, 8, 5]
    in_order_traversal(build_bst_from_preorder(preorder))
    print()
    in_order_traversal(build_bst_from_postorder(postorder))
    print()


if __name__ == "__main__":
    main()
