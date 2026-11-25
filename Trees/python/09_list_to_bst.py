from print_tree import print_tree
from tree_common import MAX_NUM_NODES_IN_TREE, Node, handle_error, is_bst, print_list


def list_to_bst(list_node, start, end):
    """Convert a sorted doubly linked list (left = prev, right = next) into a
    balanced BST in O(n).

    list_node: one-element list holding the current list node (C double ptr)
    start, end: indexes of the region of the list being operated on
    Returns: root of the BST
    """
    if start > end:
        return None
    middle = (start + end) // 2
    # build left subtree from nodes before middle
    left_child = list_to_bst(list_node, start, middle - 1)
    # list_node now points to the middle node
    middle_node = list_node[0]
    middle_node.left = left_child
    # advance to the node after middle
    list_node[0] = list_node[0].right
    middle_node.right = list_to_bst(list_node, middle + 1, end)
    return middle_node


def print_result(result):
    if result:
        print("The tree is a Binary Search Tree")
    else:
        print("The tree is NOT a Binary Search Tree")


def main():
    for num_elems in range(1, MAX_NUM_NODES_IN_TREE + 1):
        # construct a doubly linked list
        head = prev = None
        for i in range(num_elems):
            new_node = Node(i)
            new_node.left = prev
            if prev:
                prev.right = new_node
            if i == 0:
                head = new_node
            prev = new_node

        print("Printing the Doubly Linked List:")
        print_list(head)

        root = list_to_bst([head], 0, num_elems - 1)
        print("Printing tree:")
        print_tree(root, num_elems)

        result = is_bst(root, [None])
        print_result(result)
        if not result:
            handle_error()
        print("_____________________________________________________________")
    print("Test passed ")


if __name__ == "__main__":
    main()
