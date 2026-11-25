"""Binary tree level order traversal."""
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root):
        answer = []
        if root is None:
            return answer
        q = deque([(root, 1)])  # (node, level)
        while q:
            current_node, current_level = q.popleft()
            # Create a new list for a new level
            if len(answer) < current_level:
                answer.append([])
            answer[current_level - 1].append(current_node.val)
            if current_node.left:
                q.append((current_node.left, current_level + 1))
            if current_node.right:
                q.append((current_node.right, current_level + 1))
        return answer


def main():
    """
              3
            /   \\
           9     20
                /  \\
               15   7

    Expected Output
    Level 1 : 3
    Level 2 : 9 20
    Level 3 : 15 7
    """
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    result = Solution().levelOrder(root)
    print("Level Order Traversal\n")
    for i, level in enumerate(result):
        print(f"Level {i + 1} : " + "".join(f"{x} " for x in level))


if __name__ == "__main__":
    main()
