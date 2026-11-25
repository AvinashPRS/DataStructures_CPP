"""
    Given a binary tree, where the nodes contain additional info about
    the no. of nodes in its subtree. Find the Kth node in inorder traversal
    of this tree.
    Solution:
        Since each root of a subtree has info about the no. of nodes in
        its subtree, we can use that info to decide in which direction to go.
        For current root:
        if num nodes in left >= K: go left
        if num nodes in left + 1 == K, then it is root
        else go right with K -= left + 1
        TC: O(h), since at max we will go to one leaf node
        SC: O(1)
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.num_nodes = 0


def find_kth_inorder_node(root, k):
    """Finds the kth node in inorder traversal of tree."""
    curr = root
    while curr:
        left_nodes = curr.left.num_nodes if curr.left else 0
        if left_nodes >= k:            # in left subtree
            curr = curr.left
        elif left_nodes + 1 == k:      # it is the current node
            # (the C++ original returns `root` here, which is a bug)
            return curr
        else:                          # on the right, or K > total nodes
            k -= left_nodes + 1
            curr = curr.right
    print("Not found", end="")
    return None


def in_order_traversal(node):
    if node:
        in_order_traversal(node.left)
        print(node.data, end=" ")
        in_order_traversal(node.right)


def main():
    r"""
                    1
                  /   \
                2      3
               /  \   /
              4    5  6
                     /
                    7
    """
    root = Node(1)
    root.num_nodes = 7
    root.left = Node(2)
    root.left.num_nodes = 3
    root.right = Node(3)
    root.right.num_nodes = 3
    root.left.left = Node(4)
    root.left.left.num_nodes = 1
    root.left.right = Node(5)
    root.left.right.num_nodes = 1
    root.right.left = Node(6)
    root.right.left.num_nodes = 2
    root.right.left.left = Node(7)
    root.right.left.left.num_nodes = 1
    in_order_traversal(root)
    result = find_kth_inorder_node(root, 17)
    if result:
        print()
        print(result.data)
    print()
    result = find_kth_inorder_node(root, 5)
    if result:
        print("5th inorder node:", result.data)


if __name__ == "__main__":
    main()
