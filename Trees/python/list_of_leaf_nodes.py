"""
    Given a binary tree, create a linked list from the leaves of the tree, from left to right order.
    Solution:
        Start traversal in either inorder or preorder, then once leaf is reached, add to list.
        We create a list for each subtree and then append it to the previous call list.
        TC: O(n)
        SC: O(h), for recursive stack
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def create_list_from_leaves(root):
    """Returns a list of the leaf nodes from left to right."""
    leaf_list = []
    if root is None:
        return leaf_list
    if root.left is None and root.right is None:
        leaf_list.append(root)
    # leaves from the left subtree first, then from the right subtree
    leaf_list.extend(create_list_from_leaves(root.left))
    leaf_list.extend(create_list_from_leaves(root.right))
    return leaf_list


def in_order_traversal(node):
    if node:
        in_order_traversal(node.left)
        print(node.data, end=" ")
        in_order_traversal(node.right)


def build_sample_tree():
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
    return root


def main():
    root = build_sample_tree()
    in_order_traversal(root)
    print()
    head = create_list_from_leaves(root)
    print("Leaf Nodes:")
    print(" ".join(str(n.data) for n in head))


if __name__ == "__main__":
    main()
