r"""
    Given a binary tree, find the exterior nodes of binary tree. Exterior sequence:
    Nodes from root to leftmost leaf, then leftmost leaf to rightmost leaf and from there
    back to tree root.
    Solution:
        It can be done with three traversals, but TC: O(h + n + h). To avoid revisiting:
        1. add root
        2. traverse left subtree adding the left boundary (root to first leaf) and its leaves
        3. traverse right subtree adding its leaves and the right boundary (leaf to root)
        TC: O(n)
        SC: O(h), for recursive stack
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def left_boundary_and_leaves(root, first_leaf_found):
    """Adds the left boundary and the leaves of the left subtree."""
    l = []
    if root:
        if root.left is None and root.right is None:
            l.append(root)
            # after this we won't get any boundary nodes
            first_leaf_found = True
        # nodes on the path till the first leaf are boundary nodes
        if not first_leaf_found:
            l.append(root)
        l.extend(left_boundary_and_leaves(root.left, first_leaf_found))
        l.extend(left_boundary_and_leaves(root.right, first_leaf_found))
    return l


def right_leaves_and_boundary(root, right_boundary):
    """Adds the leaves of the right subtree and then the right boundary
    (bottom-up). A left child is on the boundary only when its parent is a
    boundary node without a right child."""
    l = []
    if root:
        l.extend(right_leaves_and_boundary(root.left, right_boundary and root.right is None))
        l.extend(right_leaves_and_boundary(root.right, right_boundary))
        if (root.left is None and root.right is None) or right_boundary:
            l.append(root)
    return l


def find_binary_tree_exterior(root):
    """Finds the exterior view of a binary tree."""
    exterior = [root]
    exterior.extend(left_boundary_and_leaves(root.left, False))
    exterior.extend(right_leaves_and_boundary(root.right, True))
    return exterior


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
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.left.left = Node(7)
    in_order_traversal(root)
    print()
    head = find_binary_tree_exterior(root)
    print("Leaf Nodes:")
    print(" ".join(str(n.data) for n in head))


if __name__ == "__main__":
    main()
