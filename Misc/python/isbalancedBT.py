"""Check whether a binary tree is height-balanced (LeetCode 110)."""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root):
        return self.height(root) != -1

    def height(self, node):
        """Height of the subtree, or -1 if it is not balanced."""
        if node is None:
            return 0
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        if left_height == -1 or right_height == -1 or \
                abs(left_height - right_height) > 1:
            return -1
        return max(left_height, right_height) + 1
