from print_tree import print_tree
from tree_common import MAX_NUM_NODES_IN_TREE, construct_bst


def print_data(data):
    print(data, end=" ")


def print_left_border(cur_node):
    """Keep going left and print the non-leaf nodes."""
    while cur_node:
        if cur_node.left or cur_node.right:
            print_data(cur_node.data)
        cur_node = cur_node.left


def print_leaf_nodes(cur_node):
    if cur_node is None:
        return
    if not cur_node.left and not cur_node.right:
        print_data(cur_node.data)
    print_leaf_nodes(cur_node.left)
    print_leaf_nodes(cur_node.right)


def print_right_border(cur_node):
    """Reach the deepest right node, then print non-leaf nodes bottom-up."""
    if cur_node is None:
        return
    print_right_border(cur_node.right)
    if cur_node.left or cur_node.right:
        print_data(cur_node.data)


def print_border_nodes(root):
    if root is None:
        return
    print_left_border(root)
    print_leaf_nodes(root)
    print_right_border(root)


def main():
    number_array = list(range(MAX_NUM_NODES_IN_TREE))
    for num_elems in range(1, MAX_NUM_NODES_IN_TREE + 1):
        root1 = construct_bst(None, number_array, 0, num_elems - 1)
        print("Printing tree:")
        print_tree(root1, num_elems)
        print("The border nodes are : ", end="")
        print_border_nodes(root1)
        print("\n__________________________________________")
    print("Test passed")


if __name__ == "__main__":
    main()
