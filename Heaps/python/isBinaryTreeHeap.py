"""Check if a given binary tree is a (max) heap: complete binary tree + max order."""


class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


class Solution:
    def count_nodes(self, root):
        if root is None:
            return 0
        return 1 + self.count_nodes(root.left) + self.count_nodes(root.right)

    # check if the tree is a Complete Binary Tree
    def is_cbt(self, root, index, total_count):
        if root is None:
            return True
        if index >= total_count:
            return False
        left = self.is_cbt(root.left, 2 * index + 1, total_count)
        right = self.is_cbt(root.right, 2 * index + 2, total_count)
        return left and right

    def is_max_order(self, root):
        # empty tree is a valid heap structure
        if root is None:
            return True
        if root.left is None and root.right is None:
            return True
        if root.right is None:
            return root.data > root.left.data
        left = self.is_max_order(root.left)
        right = self.is_max_order(root.right)
        return left and right and (root.data > root.left.data and root.data > root.right.data)

    # Check if the given binary tree is a heap
    def is_heap(self, root):
        total_count = self.count_nodes(root)
        return self.is_cbt(root, 0, total_count) and self.is_max_order(root)


if __name__ == "__main__":
    solver = Solution()

    #          50
    #        /    \
    #      30      40
    #     /  \    /
    #    10  20  35
    root = Node(50)
    root.left = Node(30)
    root.right = Node(40)
    root.left.left = Node(10)
    root.left.right = Node(20)
    root.right.left = Node(35)

    if solver.is_heap(root):
        print("The binary tree is a valid Max-Heap.")
    else:
        print("The binary tree is NOT a valid Max-Heap.")
