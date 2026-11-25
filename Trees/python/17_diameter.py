from print_tree import print_tree
from tree_common import MAX_NUM_NODES_IN_TREE, construct_bst

MAX_NODE_VALUE = 10


def find_diameter(cur_node, diameter):
    """Returns the height of cur_node (leaf = 1).
    diameter: one-element list - receives the number of nodes on the longest
    path between any two leaves."""
    if cur_node is None:
        return 0
    left_height = find_diameter(cur_node.left, diameter)
    right_height = find_diameter(cur_node.right, diameter)
    height = 1 + max(left_height, right_height)
    # longest path passing through cur_node
    longest_path = left_height + right_height + 1
    if longest_path > diameter[0]:
        diameter[0] = longest_path
    return height


def test():
    number_array = list(range(MAX_NUM_NODES_IN_TREE))
    for num_elems in range(1, MAX_NUM_NODES_IN_TREE + 1):
        root = construct_bst(None, number_array, 0, num_elems - 1)
        print("Printing tree:")
        print_tree(root, num_elems)
        diameter = [0]
        height = find_diameter(root, diameter)
        print("Height = %d, Diameter = %d" % (height, diameter[0]))
        print("___________________________________________________")


def main():
    test()
    print("Test passed ")


if __name__ == "__main__":
    main()
