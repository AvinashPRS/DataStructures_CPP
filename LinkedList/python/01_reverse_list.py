"""
Reverse a singly linked list, both iteratively and recursively.

Input: head of the list
Output: head of the reversed list

TC: O(n)
SC: O(1) iterative, O(n) recursive (call stack)
"""
import sys

MAX_NUM_ELEMENTS_IN_LIST = 10


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def handle_error():
    print("Test failed")
    sys.exit(1)


def print_list(head):
    cur_node = head
    while cur_node:
        print(cur_node.data, end=" ")
        cur_node = cur_node.next
    print()


def reverse_linked_list(head):
    """Reverses the linked list without using recursion.
    Returns the first node of the reversed linked list."""
    cur_node = head
    prev_node = None

    while cur_node:
        # store the next node in a temporary variable
        next_node = cur_node.next
        # reverse the link so that current node points to the previous node
        cur_node.next = prev_node
        # update the previous node to the current node
        prev_node = cur_node
        # proceed to the next node in the original linked list
        cur_node = next_node

    # once the list has been reversed, prev_node points to the new head
    return prev_node


def reverse_linked_list_r(cur_node):
    """Recursively reverses the linked list. Returns the new head."""
    if cur_node is None or cur_node.next is None:
        return cur_node  # last node in original list is the new head

    # recursively reverse the remaining nodes in the linked list
    new_head = reverse_linked_list_r(cur_node.next)

    # connect up the current node to the reversed linked list
    cur_node.next.next = cur_node
    cur_node.next = None
    return new_head


def construct_list(num_elements):
    """If num_elements = 2, the list will be 1->2->None"""
    head = None
    for value in range(num_elements, 0, -1):
        head = Node(value, head)
    return head


def run_test(title, reverse_fn):
    print(title + "\n")

    # test for different list lengths ranging from 0 to MAX_NUM_ELEMENTS_IN_LIST
    for num_elems in range(MAX_NUM_ELEMENTS_IN_LIST + 1):
        head = construct_list(num_elems)

        print("Input  : ", end="")
        print_list(head)

        head = reverse_fn(head)

        print("Output : ", end="")
        print_list(head)

        # iterate the reversed list and check if the list is in reverse order
        cur_node = head
        for j in range(num_elems):
            if cur_node.data != num_elems - j:
                handle_error()
            cur_node = cur_node.next

        print("_______________________________________________")


if __name__ == "__main__":
    run_test("Testing Non-Recursive Linked List Reversal", reverse_linked_list)
    run_test("Testing Recursive Linked List Reversal", reverse_linked_list_r)
    print("Test passed")
