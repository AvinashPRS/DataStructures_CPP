from tree_common import MAX_NUM_NODES_IN_TREE, construct_bst

MAX_NODE_VALUE = 10


def process_sum(cur_node, col, sum_array):
    """Add cur_node's data to its column, recurse with col-1 / col+1."""
    if cur_node is None:
        return
    sum_array[col] += cur_node.data
    process_sum(cur_node.left, col - 1, sum_array)
    process_sum(cur_node.right, col + 1, sum_array)


def compute_vertical_sum(root):
    """Returns the list of vertical (column) sums, left-most column first.

    Like the C version, the number of columns is derived from the left-most
    and right-most spines, which is exact for the balanced BSTs used here.
    """
    if root is None:
        return []
    num_left_cols = 0
    cur_node = root.left
    while cur_node:
        num_left_cols += 1
        cur_node = cur_node.left
    num_right_cols = 0
    cur_node = root.right
    while cur_node:
        num_right_cols += 1
        cur_node = cur_node.right

    sum_array = [0] * (num_left_cols + num_right_cols + 1)
    process_sum(root, num_left_cols, sum_array)
    return sum_array


def test_01():
    number_array = list(range(MAX_NUM_NODES_IN_TREE))
    for num_elems in range(1, MAX_NUM_NODES_IN_TREE + 1):
        root = construct_bst(None, number_array, 0, num_elems - 1)
        sum_array = compute_vertical_sum(root)
        print("Vertical sum is:" + "".join("%d " % s for s in sum_array))
        print("___________________________________________________")


def main():
    test_01()
    print("Test passed")


if __name__ == "__main__":
    main()
