from print_tree import print_tree
from tree_common import MAX_NUM_NODES_IN_TREE, construct_bst, handle_error, print_list


def bst_to_list(cur_node, prev_node, list_head):
    """In-order convert a BST into a doubly linked list (left = prev,
    right = next).
    prev_node: one-element list - node previous to cur_node in the list
    list_head: one-element list - receives the head of the list
    """
    if cur_node is None:
        return 0
    bst_to_list(cur_node.left, prev_node, list_head)
    # link previous node and current node
    cur_node.left = prev_node[0]
    if prev_node[0] is not None:
        prev_node[0].right = cur_node
    else:
        list_head[0] = cur_node  # first node of the list
    prev_node[0] = cur_node
    bst_to_list(cur_node.right, prev_node, list_head)
    return 0


def verify_list(head):
    if head is None:
        return
    # left to right: increasing order
    prev_node, iter_node, last_node = head, head.right, head
    while iter_node:
        if prev_node.data >= iter_node.data:
            handle_error()
        if iter_node.right is None:
            last_node = iter_node
        prev_node, iter_node = iter_node, iter_node.right
    # right to left: decreasing order
    prev_node, iter_node = last_node, last_node.left
    while iter_node:
        if prev_node.data <= iter_node.data:
            handle_error()
        prev_node, iter_node = iter_node, iter_node.left


def main():
    number_array = list(range(MAX_NUM_NODES_IN_TREE))
    for num_elems in range(1, MAX_NUM_NODES_IN_TREE + 1):
        root = construct_bst(None, number_array, 0, num_elems - 1)
        print("Printing tree:")
        print_tree(root, num_elems)

        head = [None]
        bst_to_list(root, [None], head)
        print("Printing the Doubly Linked List:")
        print_list(head[0])
        verify_list(head[0])
        print("___________________________________________________")
    print("Test passed ")


if __name__ == "__main__":
    main()
