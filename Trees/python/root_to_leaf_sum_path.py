"""
    Given a binary tree and a sum, find if any root to
    leaf path contains that sum.
    Solution:
        We can do any DFS traversal and while going down a level, we pass
        current_sum - curr_data; on reaching a leaf node if the sum is 0,
        then the path is found.
        TC: O(n)
        SC: O(h), for recursive stack
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def is_sum_path_possible(root, total):
    """Checks if there is any root to leaf path with the given sum."""
    if root is None:
        return False
    total -= root.data
    if root.left is None and root.right is None and total == 0:
        return True
    return is_sum_path_possible(root.left, total) or is_sum_path_possible(root.right, total)


def is_sum_path_possible_iteratively(root, total):
    """Same as above, but iteratively with an inorder walk.
    Each stack entry is (remaining sum after this node, node)."""
    s = []
    curr_sum, curr_node = total, root
    while s or curr_node:
        if curr_node:
            curr_sum -= curr_node.data
            s.append((curr_sum, curr_node))
            curr_node = curr_node.left
        else:
            curr_sum, curr_node = s.pop()
            if curr_node.left is None and curr_node.right is None and curr_sum == 0:
                return True
            curr_node = curr_node.right
    return False


def post_order_traversal(node):
    if node:
        post_order_traversal(node.left)
        post_order_traversal(node.right)
        print(node.data, end=" ")


def build_sample_tree():
    r"""
                    1
                  /   \
                2      3
               /  \   /
              4    5  6
                     /
                    7
    """
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.left.left = Node(7)
    return root


def main():
    root = build_sample_tree()
    # post_order_traversal(root)
    print()
    print(int(is_sum_path_possible(root, 17)))
    print(int(is_sum_path_possible_iteratively(root, 17)))


if __name__ == "__main__":
    main()
