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
    depth = binary_tree_depth(root)
    print("Depth of %d: %d" % (root.n, depth))
    depth = binary_tree_depth(root.right)
    print("Depth of %d: %d" % (root.right.n, depth))
    depth = binary_tree_depth(root.left.right)
    print("Depth of %d: %d" % (root.left.right.n, depth))


if __name__ == "__main__":
    main()
