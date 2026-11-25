"""Validate a Binary Search Tree using lower/upper bound nodes."""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root):
        return self._is_valid(root, None, None)

    def _is_valid(self, node, lower, upper):
        if node is None:
            return True
        if (lower is not None and node.val <= lower.val) or \
                (upper is not None and node.val >= upper.val):
            return False
        return (self._is_valid(node.left, lower, node) and
                self._is_valid(node.right, node, upper))


def report(sol, root):
    print("Tree is a Valid BST" if sol.isValidBST(root) else "Tree is NOT a Valid BST")


def main():
    sol = Solution()
    """
             8
           /   \\
          3     10
         / \\      \\
        1   6      14
           / \\     /
          4   7   13
    Valid BST
    """
    root = TreeNode(8)
    root.left = TreeNode(3)
    root.right = TreeNode(10)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(6)
    root.left.right.left = TreeNode(4)
    root.left.right.right = TreeNode(7)
    root.right.right = TreeNode(14)
    root.right.right.left = TreeNode(13)
    report(sol, root)

    """
              5
            /   \\
           1     4
                / \\
               3   6
    Invalid because 4 is in the right subtree of 5 but 4 < 5.
    """
    root2 = TreeNode(5)
    root2.left = TreeNode(1)
    root2.right = TreeNode(4)
    root2.right.left = TreeNode(3)
    root2.right.right = TreeNode(6)
    report(sol, root2)


if __name__ == "__main__":
    main()
