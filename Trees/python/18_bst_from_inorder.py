from print_tree import print_tree
from tree_common import MAX_NUM_NODES_IN_TREE, Node, construct_bst, handle_error

MAX_NODE_VALUE = 10


def print_array(array, length):
    print("".join("%d " % array[i] for i in range(length)))


def traverse_pre_order(cur_node, out):
    if cur_node is None:
        return
    out.append(cur_node.data)
    traverse_pre_order(cur_node.left, out)
    traverse_pre_order(cur_node.right, out)


def traverse_in_order(cur_node, out):
    if cur_node is None:
        return
    traverse_in_order(cur_node.left, out)
    out.append(cur_node.data)
    traverse_in_order(cur_node.right, out)


def construct_tree(pre_order, in_order, in_start, in_end, pre_pos):
    """Rebuild a binary tree from its pre-order and in-order traversals.

    in_start, in_end: current region of the in_order array
    pre_pos: one-element list - current index in the pre_order array
    """
    if in_start > in_end:
        return None
    pivot = pre_order[pre_pos[0]]
    # find pivot in the in-order array
    in_location = in_start
    while in_location <= in_end and in_order[in_location] != pivot:
        in_location += 1

    new_node = Node(pivot)
    pre_pos[0] += 1
    new_node.left = construct_tree(pre_order, in_order, in_start, in_location - 1, pre_pos)
    new_node.right = construct_tree(pre_order, in_order, in_location + 1, in_end, pre_pos)
    return new_node


def verify_trees(n1, n2):
    if n1 is None and n2 is None:
        return
    if n1 is None or n2 is None:
        handle_error()
    if n1.data != n2.data:
        handle_error()
    verify_trees(n1.left, n2.left)
    verify_trees(n1.right, n2.right)


def test_01():
    number_array = list(range(MAX_NUM_NODES_IN_TREE))
    for num_elems in range(1, MAX_NUM_NODES_IN_TREE + 1):
        root = construct_bst(None, number_array, 0, num_elems - 1)

        pre_order = []
        traverse_pre_order(root, pre_order)
        print("Pre-order is : ", end="")
        print_array(pre_order, num_elems)

        in_order = []
        traverse_in_order(root, in_order)
        print("In-order is : ", end="")
        print_array(in_order, num_elems)

        assembled_root = construct_tree(pre_order, in_order, 0, num_elems - 1, [0])
        print("Printing tree:")
        print_tree(root, num_elems)
        verify_trees(root, assembled_root)
        print("___________________________________________________________________")


def main():
    test_01()
    print("Test passed")


if __name__ == "__main__":
    main()
