"""
Remove duplicates from an unsorted linked list using a hash table.

Approach: walk the list keeping a set of values already seen; unlink any
node whose value was seen before.

TC: O(n)
SC: O(n) (O(MAX_VALUE) here, since values are in [0, MAX_VALUE))
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
    # if there are 0 or 1 nodes in the linked list, then simply return
    if head is None or head.next is None:
        return

    # hash table of values seen so far
    seen = set()

    cur_node = head
    prev_node = None
    while cur_node:
        # LOOKUP: O(1) check if the key already exists in our hash table
        if cur_node.data in seen:
            # cur_node is a duplicate. So remove it
            prev_node.next = cur_node.next
            cur_node = prev_node.next
        else:
            # INSERT: O(1) mark this key as seen
            seen.add(cur_node.data)
            prev_node = cur_node
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
