"""
Python port of print_tree.h - helper for printing a small binary tree.

Works with any node object that has `data`, `left` and `right` attributes.
"""

MAX_NUM_COLS_ON_SCREEN = 40


def fill_print_array(cur_node, cur_depth, max_depth, print_array, pos):
    """Pre-order walk that stores every node (including None) in print_array
    at heap positions (children of pos are 2*pos+1 and 2*pos+2).
    max_depth is a one-element list that receives the maximum depth."""
    print_array[pos] = cur_node
    if cur_node is None:
        return
    if cur_depth > max_depth[0]:
        max_depth[0] = cur_depth
    fill_print_array(cur_node.left, cur_depth + 1, max_depth, print_array, 2 * pos + 1)
    fill_print_array(cur_node.right, cur_depth + 1, max_depth, print_array, 2 * pos + 2)


def print_tree(root, max_num_nodes_in_tree):
    """Prints the tree level by level (only up to depth 3)."""
    if max_num_nodes_in_tree > 16:
        print("Oops, too many nodes in tree. Can't print the tree")
        return

    print_array = [None] * (1 << (max_num_nodes_in_tree + 2))
    max_depth = [-1]
    fill_print_array(root, 0, max_depth, print_array, 0)
    max_depth = max_depth[0]

    if max_depth > 3:
        print("Oops can't print the tree at depth more than 4 ")
        return

    # for depth 0, start_display_pos = 20, offset = 40 -> root printed at col 20
    # for depth 1, start_display_pos = 10, offset = 20 -> cols 10 and 30 ...
    print_index = 0
    start_display_pos = MAX_NUM_COLS_ON_SCREEN // 2
    offset = MAX_NUM_COLS_ON_SCREEN
    for cur_depth in range(max_depth + 1):
        line = []
        screen_pos = 0
        node_display_pos = start_display_pos
        for _ in range(1 << cur_depth):
            cur_node = print_array[print_index]
            while screen_pos < node_display_pos:
                line.append(" ")
                screen_pos += 1
            if cur_node is not None:
                line.append(str(cur_node.data))
                screen_pos += 1
            node_display_pos += offset
            print_index += 1
        print("".join(line))
        start_display_pos //= 2
        offset //= 2

    print("\n")
