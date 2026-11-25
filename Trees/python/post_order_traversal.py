"""
Postorder traversal is a depth-first tree traversal method where each node
is processed after its left and right children. Besides the recursive
version, there are iterative approaches:

  * Solution (iterative): push root; pop a node, prepend its value to the
    answer, push left then right child. The result is root-right-left
    reversed == left-right-root.
  * post_order (single stack, push twice): push each node twice; keep moving
    left. When popping, if the stack top is the same node, go to its right
    subtree, else output the node.
"""


class TreeNode:
    """Definition for a binary tree node."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class SolutionRecursive:
    def __init__(self):
        self.ans = []

    def postorder(self, node):
        if not node:
            return
        self.postorder(node.left)
        self.postorder(node.right)
        self.ans.append(node.val)

    def postorderTraversal(self, root):
        self.postorder(root)
        return self.ans


class Solution:
    """Iterative version."""

    def postorderTraversal(self, root):
        ans = []
        if not root:
            return ans
        stk = [root]
        while stk:
            cur = stk.pop()
            ans.append(cur.val)  # C++ inserts at the front; reverse at the end
            if cur.left:
                stk.append(cur.left)
            if cur.right:
                stk.append(cur.right)
        ans.reverse()
        return ans


def post_order(root):
    """Iterative postorder with a single stack (each node pushed twice)."""
    res = []
    st = []
    while True:
        while root:
            st.append(root)
            st.append(root)
            root = root.left
        if not st:
            return res
        root = st.pop()
        if st and st[-1] is root:
            root = root.right
        else:
            res.append(root.val)
            root = None


def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    print(" ".join(map(str, SolutionRecursive().postorderTraversal(root))))
    print(" ".join(map(str, Solution().postorderTraversal(root))))
    print(" ".join(map(str, post_order(root))))


if __name__ == "__main__":
    main()
