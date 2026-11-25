"""
Remove duplicates from an unsorted linked list without extra space.

Approach: for every node, scan the rest of the list and unlink any node
having the same data.

TC: O(n^2)
SC: O(1)
"""
import random
import sys

MAX_NUM_ELEMENTS_IN_LIST = 10
MAX_VALUE = 10


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def handle_error():
    print("Test failed")
    sys.exit(1)


def remove_duplicates(head):
    """head: first node in the linked list"""
    # if there are 0 or 1 nodes in linked list, then simply return
    if head is None or head.next is None:
        return

    cur_node = head
    while cur_node:
        # iterate from node after cur_node to the end of the linked list
        iter_node = cur_node.next
        prev_node = cur_node

        while iter_node:
            if cur_node.data == iter_node.data:
                # iter_node is a duplicate of cur_node. So remove it
                prev_node.next = iter_node.next
                iter_node = prev_node.next
            else:
                prev_node = iter_node
                iter_node = iter_node.next

        cur_node = cur_node.next


def construct_list(num_elements):
    head = None
    for _ in range(num_elements):
        head = Node(random.randrange(MAX_VALUE), head)
    return head


def print_list(head):
    cur_node = head
    while cur_node:
        print(cur_node.data, end=" ")
        cur_node = cur_node.next
    print()


def verify_list(head):
    """Flags an error if the list still contains duplicates."""
    cur_node = head
    while cur_node:
        iter_node = cur_node.next
        while iter_node:
            if cur_node.data == iter_node.data:
                handle_error()
            iter_node = iter_node.next
        cur_node = cur_node.next


if __name__ == "__main__":
    # test for different list lengths
    for num_elems in range(MAX_NUM_ELEMENTS_IN_LIST + 1):
        # construct a list with random elements. The list can contain duplicates
        head = construct_list(num_elems)

        print("Input  : ", end="")
        print_list(head)

        remove_duplicates(head)

        print("Output : ", end="")
        print_list(head)

        verify_list(head)

        print("__________________________________________________________")

    print("Test passed ")
