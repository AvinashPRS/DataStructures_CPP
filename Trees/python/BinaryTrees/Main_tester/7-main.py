import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from binary_trees import *  # noqa: E402,F401,F403


def print_num(n):
    print(n)


def main():
    root = binary_tree_node(None, 98)
    root.left = binary_tree_node(root, 12)
    root.right = binary_tree_node(root, 402)
    root.left.left = binary_tree_node(root.left, 6)
    root.left.right = binary_tree_node(root.left, 56)
    root.right.left = binary_tree_node(root.right, 256)
    root.right.right = binary_tree_node(root.right, 512)
    binary_tree_print(root)
    binary_tree_inorder(root, print_num)


if __name__ == "__main__":
    main()
