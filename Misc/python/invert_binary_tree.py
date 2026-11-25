"""Invert (mirror) a binary tree."""
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def invertTree(self, root):
        return self._invert(root)

    def _invert(self, node):
        if node is not None:
            left = self._invert(node.left)    # invert left subtree
            right = self._invert(node.right)  # invert right subtree
            node.left, node.right = right, left  # swap them
        return node


def inorder(root, out=None):
    if out is None:
        out = []
    if root:
        inorder(root.left, out)
        out.append(root.val)
        inorder(root.right, out)
    return out


def level_order(root):
    if root is None:
        return
    q = deque([root])
    while q:
        line = ""
        for _ in range(len(q)):
            node = q.popleft()
            line += f"{node.val} "
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        print(line)


def main():
    """
             4
           /   \\
          2     7
         / \\   / \\
        1  3  6   9
    """
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)

    print("Original Tree (Level Order)\n")
    level_order(root)
    root = Solution().invertTree(root)
    print("\nInverted Tree (Level Order)\n")
    level_order(root)


if __name__ == "__main__":
    main()
