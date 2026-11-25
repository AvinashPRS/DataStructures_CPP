r"""
    Given a perfect binary tree with extra right_sibling field, which should point to the
    right node in that level. Initially this extra field is empty for all the nodes; make
    the extra field point to the correct locations.
    Solution:
        Can be done in two ways:
        1. Simple BFS: for each level, link the previous node of the level to the current.
        2. Since this is a perfect binary tree, for a left child its right sibling is the
           right child of its parent and for the right child it is the left child of the
           parent's right sibling (if it exists, else None).
        TC: O(n)
        SC: BFS: O(n), method 2: O(1)
"""
from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.right_sibling = None


def join_right_siblings_bfs(root):
    """Joins the right siblings using simple BFS."""
    q = deque([root])
    prev = None
    level_count = len(q)
    while q:
        curr = q.popleft()
        level_count -= 1
        if curr.left:
            q.append(curr.left)
        if curr.right:
            q.append(curr.right)
        if prev is not None:
            prev.right_sibling = curr
        prev = curr
        # last node of current level
        if level_count == 0:
            level_count = len(q)
            prev = None


def join_right_siblings_in_same_level(parent):
    """Joins the children of every node in parent's level."""
    while parent:
        parent.left.right_sibling = parent.right
        if parent.right_sibling:
            parent.right.right_sibling = parent.right_sibling.left
        parent = parent.right_sibling


def join_right_siblings(root):
    """Joins the right siblings using the O(1)-space (EPI) method."""
    it = root
    while it and it.left:
        join_right_siblings_in_same_level(it)
        it = it.left


def print_right_siblings(root):
    it = root
    while it:
        level_iter = it
        out = []
        while level_iter:
            out.append(str(level_iter.right_sibling.data) if level_iter.right_sibling else "NULL")
            level_iter = level_iter.right_sibling
        print(" ".join(out) + " ")
        it = it.left


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
               /  \   /  \
              4    5  6   7
    """
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    in_order_traversal(root)
    print()
    # join_right_siblings(root)
    join_right_siblings_bfs(root)
    print_right_siblings(root)


if __name__ == "__main__":
    main()
