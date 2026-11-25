"""Check whether a binary tree is a mirror of itself."""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root):
        if root is None:
            return True
        return self._is_sym(root.left, root.right)

    def _is_sym(self, left_tree, right_tree):
        if left_tree is None and right_tree is None:  # both empty
            return True
        if left_tree is None or right_tree is None:   # one empty
            return False
        if left_tree.val != right_tree.val:           # values differ
            return False
        # mirror comparison
        return (self._is_sym(left_tree.left, right_tree.right) and
                self._is_sym(left_tree.right, right_tree.left))


def main():
    """
                1
              /   \\
             2     2
            / \\   / \\
           3   4 4   3
    """
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)

    sol = Solution()
    print("Tree is Symmetric" if sol.isSymmetric(root) else "Tree is NOT Symmetric")

    # Make the tree asymmetric
    root.right.right = None
    print("Tree is Symmetric" if sol.isSymmetric(root) else "Tree is NOT Symmetric")


if __name__ == "__main__":
    main()
