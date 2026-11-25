"""
Clone a linked list where each node has a next pointer and a random pointer
(the random pointer can point to any node in the list).

Approach (no hash table):
    1. Create a copy of each node and place it right after the original node.
    2. Set copy.random = original.random.next
    3. Separate the copies from the original list.

TC: O(n)
SC: O(1) extra (apart from the cloned list)
"""
import random
import sys

MAX_NUM_ELEMENTS_IN_LIST = 10


class Node:
    def __init__(self, data, next=None, random=None):
        self.data = data
        self.next = next
        self.random = random


def handle_error():
    print("Test failed")
    sys.exit(1)


def clone_list(original_head):
    """Returns head of the newly created linked list"""
    new_head = None

    # for each node in the original list, create a new node and place it
    # next to the original node
    n1 = original_head
    while n1:
        next_node = n1.next
        n2 = Node(n1.data, next_node)
        if new_head is None:
            new_head = n2
        n1.next = n2
        n1 = next_node

    # set the random pointer correctly for the new nodes
    n1 = original_head
    while n1:
        n1.next.random = n1.random.next
        n1 = n1.next.next

    # disconnect the new nodes from the original list and form a new list for them
    n1 = original_head
    while n1:
        n2 = n1.next
        n1.next = n1.next.next
        if n2.next:
            n2.next = n2.next.next
        n1 = n1.next

    return new_head


def construct_list(num_elements):
    """If num_elements = 2, the list created will be 1->2.
    Each node's random pointer points to a random node in the list."""
    nodes = [Node(value) for value in range(1, num_elements + 1)]
    for i in range(num_elements - 1):
        nodes[i].next = nodes[i + 1]

    # connect each node in the list to a random node
    for node in nodes:
        node.random = random.choice(nodes)

    return nodes[0] if nodes else None


if __name__ == "__main__":
    # test for different list lengths
    for num_elems in range(MAX_NUM_ELEMENTS_IN_LIST + 1):
        head = construct_list(num_elems)

        clone = clone_list(head)

        # verify if the clone is a proper copy of the original list
        n1, n2 = head, clone
        while n1 and n2:
            if n1 is n2 or n1.data != n2.data or n1.random.data != n2.random.data:
                handle_error()
            n1 = n1.next
            n2 = n2.next

        # if the original list or the clone is longer than the other, report error
        if n1 or n2:
            handle_error()

    print("Test passed")
