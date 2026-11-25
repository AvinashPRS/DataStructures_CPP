"""
Copyright (C) 2017 Interview Druid, Parineeth M. R.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
"""
import sys

from print_tree import print_tree

MAX_NUM_NODES_IN_TREE = 10
MAX_NODE_VALUE = 10


class Node:
    def __init__(self, data=0, parent=None):
        self.data = data
        self.depth = parent.depth + 1 if parent else 0
        self.left = None
        self.right = None
        self.parent = parent


def construct_bst(parent, values, low, high):
    if low > high:
        return None
    middle = (low + high) // 2
    new_node = Node(values[middle], parent)
    new_node.left = construct_bst(new_node, values, low, middle - 1)
    new_node.right = construct_bst(new_node, values, middle + 1, high)
    return new_node


def print_data(data):
    print(data, end=" ")


def handle_error():
    print("Test failed")
    sys.exit(1)


def process_stacks(print_stack, store_stack, left_to_right):
    """Pop and print everything from print_stack, pushing children into
    store_stack (left first if left_to_right else right first)."""
    while print_stack:
        cur_node = print_stack.pop()
        print_data(cur_node.data)
        if left_to_right:
            if cur_node.left:
                store_stack.append(cur_node.left)
            if cur_node.right:
                store_stack.append(cur_node.right)
        else:
            if cur_node.right:
                store_stack.append(cur_node.right)
            if cur_node.left:
                store_stack.append(cur_node.left)


def print_zig_zag(root, s0, s1):
    """Print the tree spirally using two stacks (python lists)."""
    if root is None:
        return
    s0.append(root)
    while s0:
        process_stacks(s0, s1, 1)
        print()
        process_stacks(s1, s0, 0)
        print()


def test_01():
    number_array = list(range(MAX_NUM_NODES_IN_TREE))
    s1, s2 = [], []
    for num_elems in range(1, MAX_NUM_NODES_IN_TREE + 1):
        root = construct_bst(None, number_array, 0, num_elems - 1)
        print("Printing tree:")
        print_tree(root, num_elems)
        print("Zig Zag order is:")
        print_zig_zag(root, s1, s2)
        print("___________________________________________________")


def main():
    test_01()
    print("Test passed")


if __name__ == "__main__":
    main()
