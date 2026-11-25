"""
    Given a BST and a value K, find the K largest elements.
    Solution:
        Traverse right, root and then left (reverse inorder). This way we get to the
        rightmost first, then fall back to the next largest. Stop after k elements.
        TC: O(h + k)
        SC: O(h)
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def find_k_largest_elements_helper(root, k, result):
    """k: one-element list holding how many elements are still needed."""
    if root is None:
        return
    if k[0] > 0:
        # reverse inorder gives a descending sequence
        find_k_largest_elements_helper(root.right, k, result)
        if k[0] > 0:
            k[0] -= 1
            result.append(root.data)
        find_k_largest_elements_helper(root.left, k, result)


def find_k_largest_elements(root, k):
    result = []
    find_k_largest_elements_helper(root, [k], result)
    return result


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
    print(" ".join(map(str, find_k_largest_elements(root, 2))))


if __name__ == "__main__":
    main()
