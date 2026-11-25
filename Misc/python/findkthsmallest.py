"""Kth smallest element in a BST - recursive inorder traversal."""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.count = 0

    def kthSmallest(self, root, k):
        return self._inorder(root, k)

    def _inorder(self, node, k):
        if node is None:
            return -1
        # Search left subtree
        left = self._inorder(node.left, k)
        if left != -1:
            return left
        # Visit current node
        self.count += 1
        if self.count == k:
            return node.val
        # Search right subtree
        return self._inorder(node.right, k)


def build_tree():
    """
               5
             /   \\
            3     7
           / \\   / \\
          2   4 6   8
         /
        1

    Inorder: 1 2 3 4 5 6 7 8
    """
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(7)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.left.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(8)
    return root


def main():
    k = 5
    print(f"Kth smallest = {Solution().kthSmallest(build_tree(), k)}")


if __name__ == "__main__":
    main()
