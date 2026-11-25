"""Binary tree right side view, with a test harness."""
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rightSideView(self, root):
        result = []
        if root is None:
            return result
        q = deque([root])
        while q:
            size = len(q)
            for i in range(size):
                node = q.popleft()
                # Last node in this level
                if i == size - 1:
                    result.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return result


def main():
    """
            1
          /   \\
         2     3
          \\     \\
           5     4

    Right Side View: 1 3 4
    """
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(4)

    ans = Solution().rightSideView(root)
    print("Right Side View:")
    print("".join(f"{x} " for x in ans))


if __name__ == "__main__":
    main()
