r"""
    Given a tree with binary digits as data. Root represents MSB and leaf
    represents LSB. So each root to leaf path forms one number. Find the sum of all
    the numbers which can be formed from root to leaves.
    Solution:
        Starting from root, multiply the number formed till that level by 2 and add
        the digit of the current node; by the time we reach the leaf we have the
        complete number.
        TC: O(n)
        SC: O(h), for recursive stack
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def root_to_leaf_sum(root, total):
    if root is None:
        return 0
    total = total * 2 + root.data  # or (total << 1) | bit
    if root.left is None and root.right is None:
        return total
    return root_to_leaf_sum(root.left, total) + root_to_leaf_sum(root.right, total)


def find_root_to_leaf_sum(root):
    """Finds the sum of all root to leaf paths."""
    return root_to_leaf_sum(root, 0)


def post_order_traversal(node):
    if node:
        post_order_traversal(node.left)
        post_order_traversal(node.right)
        print(node.data, end=" ")


def main():
    r"""
                    1
                  /   \
                0      1
               /  \   /
              0    1  1
                     /
                    0
    """
    root = Node(1)
    root.left = Node(0)
    root.right = Node(1)
    root.left.left = Node(0)
    root.left.right = Node(1)
    root.right.left = Node(1)
    root.right.left.left = Node(0)
    post_order_traversal(root)
    print()
    print("Total Sum:", find_root_to_leaf_sum(root))


if __name__ == "__main__":
    main()
