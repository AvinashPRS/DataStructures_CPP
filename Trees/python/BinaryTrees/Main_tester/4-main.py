import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from binary_trees import *  # noqa: E402,F401,F403


def main():
    root = binary_tree_node(None, 98)
    root.left = binary_tree_node(root, 12)
    root.right = binary_tree_node(root, 402)
    binary_tree_insert_right(root.left, 54)
    binary_tree_insert_right(root, 128)
    binary_tree_print(root)
    ret = binary_tree_is_leaf(root)
    print("Is %d a leaf: %d" % (root.n, ret))
    ret = binary_tree_is_leaf(root.right)
    print("Is %d a leaf: %d" % (root.right.n, ret))
    ret = binary_tree_is_leaf(root.right.right)
    print("Is %d a leaf: %d" % (root.right.right.n, ret))


if __name__ == "__main__":
    main()
