"""
Detect a loop in a linked list and find the first node of the loop
(Floyd's cycle detection).

Approach: move a fast pointer 2 steps and a slow pointer 1 step at a time.
If they meet, there is a loop. Then move a pointer from head and the meeting
pointer one step at a time; they meet at the start of the loop.

TC: O(n)
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


def find_loop(head):
    """Returns first node in loop if loop exists, None otherwise"""
    n1 = n2 = head  # n1: fast pointer, n2: slow pointer
    found_loop = False

    while n1:
        n1 = n1.next
        if n1:
            n1 = n1.next  # fast pointer moves two steps
            n2 = n2.next  # slow pointer moves one step

        # if n1 and n2 meet then there is a loop in the linked list
        if n1 is n2:
            found_loop = True
            break

    if not found_loop:
        return None

    # find the beginning of the loop
    n3 = head
    while n1 is not n3:
        n1 = n1.next
        n3 = n3.next

    return n1


def construct_list(num_elements):
    """If num_elements = 2, the list will be 0->1"""
    head = None
    for value in range(num_elements - 1, -1, -1):
        head = Node(value, head)
    return head


def add_loop_to_list(head, num_elems):
    """Adds a loop to the linked list at a random position.
    Returns the first node in the loop"""
    # randomly generate 2 values such that low <= high
    low, high = sorted((random.randrange(num_elems), random.randrange(num_elems)))

    # find the nodes at positions low and high
    ptr1 = ptr2 = None
    cur_node = head
    i = 0
    while cur_node:
        if i == low:
            ptr1 = cur_node
        if i == high:
            ptr2 = cur_node
            break
        i += 1
        cur_node = cur_node.next

    print(f"Adding loop from pos {high} to pos {low}")

    # add loop from node at position high to node at position low
    ptr2.next = ptr1
    return ptr1


def test_01():
    # test for different list lengths
    for num_elems in range(MAX_NUM_ELEMENTS_IN_LIST + 1):
        print(f"Number of elements = {num_elems}")

        # construct the list without any loops
        head = construct_list(num_elems)

        # currently there are no loops in the list. If we find a loop, report error
        if find_loop(head):
            handle_error()

        if head:
            # add a loop to the list
            expected_loop_begin = add_loop_to_list(head, num_elems)

            # we should find the loop in the list
            result = find_loop(head)
            if result is not expected_loop_begin:
                handle_error()

            print(f"Found loop in list starting at node {result.data}")

        print("____________________________________________________")


if __name__ == "__main__":
    test_01()
    print("Test passed")
