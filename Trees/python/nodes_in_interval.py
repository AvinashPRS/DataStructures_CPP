"""
    Given a BST and an interval range [a, b]. Find all the nodes which lie in this range.
    Solution:
        Since this is a BST, we can prune while searching. If a node is smaller than the
        lower bound, its left subtree cannot have any node in the interval. Similarly if
        the node is greater than the upper bound, its right subtree cannot have any node in
        the interval. If the node lies in the range we search both its subtrees.
        TC: O(h + m), m: nodes lying in that range
        SC: O(h)
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def find_interval_nodes_helper(root, interval, result):
    if root is None:
        return
    if interval[0] <= root.data <= interval[1]:
        result.append(root)
        find_interval_nodes_helper(root.left, interval, result)
        find_interval_nodes_helper(root.right, interval, result)
    elif root.data < interval[0]:
        find_interval_nodes_helper(root.right, interval, result)
    else:
        find_interval_nodes_helper(root.left, interval, result)


def find_interval_nodes(root, interval):
    """Finds all the BST nodes that lie in the given (low, high) interval."""
    result = []
    find_interval_nodes_helper(root, interval, result)
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
    result = find_interval_nodes(root, (2, 4))
    print()
    print(" ".join(str(n.data) for n in result))


if __name__ == "__main__":
    main()
