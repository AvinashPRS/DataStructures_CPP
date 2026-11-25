"""
Given a binary tree. Print the nodes at same height, starting from top and left to right.
Input: root of binary tree
Output: list of levels

Solution:
    We can use a queue for doing BFS and keep track when a level is ending, then push the elements of that
    level to a list.
    TC: O(n), n: no. of nodes
    SC: O(m), for queue, m: max nodes in any level
"""
from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def nodes_at_same_level(root):
    """Returns a 2D layout of nodes grouped by level."""
    if root is None:
        return []

    tree_nodes = []
    q = deque([root])

    while q:
        level_size = len(q)  # number of nodes in the current level
        current_level = []

        for _ in range(level_size):
            curr = q.popleft()
            current_level.append(curr.data)

            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)

        tree_nodes.append(current_level)

    return tree_nodes


def print_levels(levels):
    for level in levels:
        print("".join(f"{el} " for el in level))


if __name__ == "__main__":
    root = Node(1)

    root.left = Node(2)
    root.right = Node(3)

    root.left.left = Node(4)
    root.left.right = Node(5)

    root.right.left = Node(6)
    root.right.right = Node(7)

    root.right.right.right = Node(8)

    print_levels(nodes_at_same_level(root))
