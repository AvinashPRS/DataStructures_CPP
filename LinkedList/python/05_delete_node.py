"""
Delete a node from a linked list when only a reference to that node is given
(head is not available). The last node cannot be deleted this way.

Approach: copy the data of the next node into the current node and unlink
the next node.

TC: O(1)
SC: O(1)
"""
import random
import sys

MAX_NUM_ELEMENTS_IN_LIST = 10


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def handle_error():
    print("Test failed")
    sys.exit(1)


def delete_node(n1):
    """n1: the node to be deleted
    Returns 0 on success, -1 on failure"""
    if n1.next:
        # get the next node
        n2 = n1.next

        # copy the contents of the next node into the current node
        n1.data = n2.data
        n1.next = n2.next

        # n2 is now unreachable and will be garbage collected
        return 0

    # the last node can't be deleted with this approach
    return -1


def construct_list(num_elements):
    """If num_elements = 2, the list will be 1->2"""
    head = None
    for value in range(num_elements, 0, -1):
        head = Node(value, head)
    return head


def print_list(head):
    cur_node = head
    while cur_node:
        print(cur_node.data, end=" ")
        cur_node = cur_node.next
    print()


if __name__ == "__main__":
    # test for different list lengths
    for num_elems in range(2, MAX_NUM_ELEMENTS_IN_LIST + 1):
        head = construct_list(num_elems)

        # choose a random position to delete. It should not be the last element
        k = random.randrange(num_elems - 1)

        print(f"Deleting {k}th node ")
        print("Input  : ", end="")
        print_list(head)

        # find the node at position k
        cur_node = head
        for _ in range(k):
            cur_node = cur_node.next

        # delete the node
        ret_val = delete_node(cur_node)

        print("Output : ", end="")
        print_list(head)

        # verify the result
        if ret_val != 0:
            handle_error()

        print("_____________________________________________")

    print("Test passed")
