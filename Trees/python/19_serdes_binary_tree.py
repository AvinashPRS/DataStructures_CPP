import os
import tempfile

from tree_common import MAX_NUM_NODES_IN_TREE, Node, construct_bst, handle_error

SPECIAL_VALUE = -1


def serialize_tree(cur_node, fp):
    """Pre-order write of the tree to fp, SPECIAL_VALUE marks a NULL child."""
    if cur_node is None:
        fp.write("%d\n" % SPECIAL_VALUE)
        return 0
    fp.write("%d\n" % cur_node.data)
    serialize_tree(cur_node.left, fp)
    serialize_tree(cur_node.right, fp)
    return 0


def deserialize_tree(fp):
    """Rebuild the tree from the file written by serialize_tree."""
    value = int(fp.readline())
    if value == SPECIAL_VALUE:
        return None
    new_node = Node(value)
    new_node.left = deserialize_tree(fp)
    new_node.right = deserialize_tree(fp)
    return new_node


def are_trees_identical(n1, n2):
    if n1 is None and n2 is None:
        return 1
    if n1 is None or n2 is None:
        return 0
    if n1.data != n2.data:
        return 0
    if not are_trees_identical(n1.left, n2.left):
        return 0
    if not are_trees_identical(n1.right, n2.right):
        return 0
    return 1


def main():
    number_array = list(range(MAX_NUM_NODES_IN_TREE))
    path = os.path.join(tempfile.gettempdir(), "serial_tree.txt")
    for num_elems in range(1, MAX_NUM_NODES_IN_TREE + 1):
        root1 = construct_bst(None, number_array, 0, num_elems - 1)
        with open(path, "w") as fp:
            serialize_tree(root1, fp)
        with open(path, "r") as fp:
            root2 = deserialize_tree(fp)
        if not are_trees_identical(root1, root2):
            handle_error()
    os.remove(path)
    print("Test passed ")


if __name__ == "__main__":
    main()
