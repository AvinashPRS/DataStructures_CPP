"""
    Given a binary tree, check if it is a BST.
    Solution:
        There are multiple ways of doing this:
        1.  Do inorder traversal of the tree, check if each element is greater than its
            previous element. Inorder traversal of a BST is a sorted array.
        2.  For each root, there is a range of values for its left and right subtree elements.
            Each time we go down, we pass the updated range; if any element doesn't fall in
            the range, then not BST (DFS).
        3.  Same range technique but with BFS, so a conflicting node high up in the tree is
            found without exploring deep subtrees first.
        TC: O(n)
        SC: DFS: O(h)
            BFS: O(n) or O(2^h + 1), last level with leaf nodes
"""
from collections import deque

INT_MIN, INT_MAX = -2 ** 31, 2 ** 31 - 1


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def check_bst_using_dfs_helper(root, lower_limit, upper_limit):
    if root is None:
        return True
    if root.data < lower_limit or root.data > upper_limit:
        return False
    return (check_bst_using_dfs_helper(root.left, lower_limit, root.data - 1) and
            check_bst_using_dfs_helper(root.right, root.data + 1, upper_limit))


def check_bst_using_dfs(root):
    """Checks if a binary tree is a BST using DFS."""
    return check_bst_using_dfs_helper(root, INT_MIN, INT_MAX)


def check_bst_using_bfs(root):
    """Checks if a binary tree is a BST using BFS.
    Queue entries are (node, lower_limit, upper_limit)."""
    q = deque([(root, INT_MIN, INT_MAX)])
    while q:
        node, lower_limit, upper_limit = q.popleft()
        if node.data > upper_limit or node.data < lower_limit:
            return False
        if node.left:
            q.append((node.left, lower_limit, node.data - 1))
        if node.right:
            q.append((node.right, node.data + 1, upper_limit))
    return True


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
    print(int(check_bst_using_bfs(root)))
    print(int(check_bst_using_dfs(root)))


if __name__ == "__main__":
    main()
