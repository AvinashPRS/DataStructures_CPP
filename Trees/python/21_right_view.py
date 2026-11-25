from print_tree import print_tree
from tree_common import MAX_NUM_NODES_IN_TREE, construct_bst


def print_data(data):
    print(data, end=" ")


def print_right_view(cur_node, cur_level, max_level):
    """
    cur_level: depth of the current node (root = 0)
    max_level: one-element list - maximum level printed so far (start at -1)
    """
    if cur_node is None:
        return
    # first node seen on this level -> print it
    if max_level[0] < cur_level:
        print_data(cur_node.data)
        max_level[0] = cur_level
    # expand right child first, then left
    print_right_view(cur_node.right, cur_level + 1, max_level)
    print_right_view(cur_node.left, cur_level + 1, max_level)


def main():
    number_array = list(range(MAX_NUM_NODES_IN_TREE))
    for num_elems in range(1, MAX_NUM_NODES_IN_TREE + 1):
        root1 = construct_bst(None, number_array, 0, num_elems - 1)
        print("Printing tree:")
        print_tree(root1, num_elems)
        print("The right view nodes are : ", end="")
        print_right_view(root1, 0, [-1])
        print("\n__________________________________________")
    print("Test passed")


if __name__ == "__main__":
    main()
