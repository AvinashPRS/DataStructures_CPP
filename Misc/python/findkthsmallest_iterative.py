"""Kth smallest element in a BST - iterative inorder traversal with a stack."""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def kthSmallest(self, root, k):
        st = []
        curr = root
        while curr is not None or st:
            # Go to leftmost node
            while curr is not None:
                st.append(curr)
                curr = curr.left
            curr = st.pop()
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right
        return -1


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
