"""
    Given a BST and three BST nodes, check if the tree nodes are ordered.
    The nodes are said to be ordered if either the first/third node is an ancestor of
    the middle node and the remaining node is a descendant of the middle.
    Solution:
        Start the search for the middle from both the outer nodes simultaneously. If one
        of them finds the other outer node, then not ordered; if it finds the middle, then
        we search from the middle for the other node. If the depth diff between the two
        nodes is 'd', it takes O(d) if they are ordered, and O(h) in the worst case.
        TC: O(d) for successful case, O(h) if nodes are not ordered
        SC: O(1)
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def are_nodes_ordered(root, node1, node2, node3):
    """Checks if three nodes of a BST are ordered or not."""
    iter1, iter2 = node1, node3
    # search for node2 from both ends; stop when node2 is found, the
    # searches bump into each other, or a leaf is passed
    while (iter1 and iter2 and iter1 is not node3 and iter2 is not node1 and
           iter1 is not node2 and iter2 is not node2):
        iter1 = iter1.left if iter1.data > node2.data else iter1.right
        iter2 = iter2.left if iter2.data > node2.data else iter2.right

    # neither found node2 -> not ordered
    if iter1 is not node2 and iter2 is not node2:
        return False

    # one outer node is an ancestor of node2, search for the other from node2
    descendant = node3 if iter1 is node2 else node1
    it = node2
    while it and it is not descendant:
        it = it.left if it.data > descendant.data else it.right
    return it is not None


def in_order_traversal(node):
    if node:
        in_order_traversal(node.left)
        print(node.data, end=" ")
        in_order_traversal(node.right)


def build_sample_bst():
    r"""
                    5
                  /   \
                2      8
               /  \   /  \
              1    3  7   9
                     /
                    6
    """
    root = Node(5)
    root.left = Node(2)
    root.right = Node(8)
    root.left.left = Node(1)
    root.left.right = Node(3)
    root.right.left = Node(7)
    root.right.left.left = Node(6)
    root.right.right = Node(9)
    return root


def main():
    root = build_sample_bst()
    in_order_traversal(root)
    # 2, 7, 6
    print()
    print(int(are_nodes_ordered(root, root.left, root.right.left, root.right.left.left)))


if __name__ == "__main__":
    main()
