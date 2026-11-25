"""
    Given a sorted array, construct a BST of minimum height.
    Solution:
        Tree will be of minimum height when the subtrees have comparable number of nodes.
        So each time we can select the middle element of array as the root and recurse on
        the left and right subarrays for left and right subtrees respectively.
        TC: T(n) = 2T(n/2) + O(1) ~ O(n)
        SC: O(n), for n sized array
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def construct_bst_from_array_helper(arr, l, h):
    if l > h:
        return None
    # select the middle element as the root
    middle_idx = l + (h - l) // 2
    root = Node(arr[middle_idx])
    root.left = construct_bst_from_array_helper(arr, l, middle_idx - 1)
    root.right = construct_bst_from_array_helper(arr, middle_idx + 1, h)
    return root


def construct_bst_from_array(arr):
    """Constructs a BST of min height."""
    return construct_bst_from_array_helper(arr, 0, len(arr) - 1)


def in_order_traversal(node):
    if node:
        in_order_traversal(node.left)
        print(node.data, end=" ")
        in_order_traversal(node.right)


def main():
    arr = [1, 2, 3, 5, 6, 7, 8]
    root = construct_bst_from_array(arr)
    in_order_traversal(root)
    print()


if __name__ == "__main__":
    main()
