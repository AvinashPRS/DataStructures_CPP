"""
Copyright (C) 2017 Interview Druid, Parineeth M. R.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
"""
import sys

from print_tree import print_tree

MAX_NUM_NODES_IN_TREE = 10


def handle_error():
    print("Test failed")
    sys.exit(1)


class Node:
    def __init__(self, data=0, parent=None):
        self.data = data
        self.depth = parent.depth + 1 if parent else 0
        self.left = None
        self.right = None
        self.parent = parent


def construct_bst(parent, values, low, high, node_array):
    """Construct a BST and also store node for values[i] in node_array[i]."""
    if low > high:
        return None
    middle = (low + high) // 2
    new_node = Node(values[middle], parent)
    new_node.left = construct_bst(new_node, values, low, middle - 1, node_array)
    new_node.right = construct_bst(new_node, values, middle + 1, high, node_array)
    node_array[middle] = new_node
    return new_node


def bst_lca(ancestor, n1, n2):
    """Least Common Ancestor in a BINARY SEARCH TREE."""
    if not ancestor or not n1 or not n2:
        return None
    # ancestor data between n1 and n2 -> it is the LCA
    if n1.data <= ancestor.data <= n2.data:
        return ancestor
    if n2.data <= ancestor.data <= n1.data:
        return ancestor
    if ancestor.data > n1.data and ancestor.data > n2.data:
        return bst_lca(ancestor.left, n1, n2)
    return bst_lca(ancestor.right, n1, n2)


def find_depth(n):
    depth = 0
    while n.parent:
        n = n.parent
        depth += 1
    return depth


def lca(n1, n2):
    """Least Common Ancestor in a BINARY TREE (using parent pointers)."""
    depth1 = find_depth(n1)
    depth2 = find_depth(n2)
    # move the deeper node up till depths match
    while depth1 > depth2:
        n1 = n1.parent
        depth1 -= 1
    while depth2 > depth1:
        n2 = n2.parent
        depth2 -= 1
    # move both up until a common node is found
    while n1 is not n2:
        n1 = n1.parent
        n2 = n2.parent
    return n1


def main():
    number_array = list(range(MAX_NUM_NODES_IN_TREE))
    node_array = [None] * MAX_NUM_NODES_IN_TREE
    for num_elems in range(1, MAX_NUM_NODES_IN_TREE + 1):
        root = construct_bst(None, number_array, 0, num_elems - 1, node_array)
        print("Printing the tree:")
        print_tree(root, num_elems)
        for i in range(num_elems):
            for j in range(i + 1, num_elems):
                lca1 = lca(node_array[i], node_array[j])
                lca2 = bst_lca(root, node_array[i], node_array[j])
                if lca1 is not lca2:
                    handle_error()
                print("Least Common Ancestor of %d and %d = %d" %
                      (node_array[i].data, node_array[j].data, lca1.data))
        print("____________________________________________________")
    print("Test passed ")


if __name__ == "__main__":
    main()
