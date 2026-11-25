"""
Rotate a linked list to the right by k positions.
eg: 1->2->3->4->5, k = 2  ==>  4->5->1->2->3

Input: head of the list, k, length of the list
Output: head of the rotated list

TC: O(n)
SC: O(1)
"""
import sys


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


def construct_list(num_elements):
    """If num_elements = 2, the list will be 1->2"""
    head = None
    for value in range(num_elements, 0, -1):
        head = Node(value, head)
    return head


def find_kth_node_from_end(head, k, length):
    """Returns (kth node from end, node previous to it).
    Returns (None, None) if the kth node doesn't exist."""
    n1 = head
    prev = None
    for i in range(1, length + 1):
        if i == length - k + 1:
            return n1, prev  # n1 is the kth element from end
        prev = n1
        n1 = n1.next
    return None, None


def rotate_list(head, k, length):
    """head: first node of the linked list
    k: by how many positions the linked list should be rotated
    length: number of nodes in the linked list
    Returns first node of the rotated linked list"""
    # if there are 0 or 1 nodes in the linked list, then simply return
    if length < 2:
        return head

    # if we shift by length times, we get back the same linked list.
    # So we just have to shift k % length times
    k = k % length

    # if k is 0, then no need to shift
    if k == 0:
        return head

    # find the kth node from the end. If k = 1, then pivot will be the last
    # node and prev will be the node previous to the last node
    pivot, prev = find_kth_node_from_end(head, k, length)

    # find the last node in the linked list
    last = pivot
    while last.next:
        last = last.next

    # make the last node point to head and the node previous to pivot point to None
    last.next = head
    prev.next = None

    # pivot will be the new head
    return pivot


def compare_list(head, expected_result):
    cur_node = head
    for value in expected_result:
        if cur_node is None or cur_node.data != value:
            handle_error()
        cur_node = cur_node.next

    if cur_node is not None:
        handle_error()


def perform_test(length, num_rotations, expected_result):
    head = construct_list(length)

    print(f"Num Rotations = {num_rotations}")

    print("Before Rotating: ", end="")
    print_list(head)

    head = rotate_list(head, num_rotations, length)
    compare_list(head, expected_result)

    print("After  Rotating: ", end="")
    print_list(head)

    print("________________________________________")


if __name__ == "__main__":
    # list initially contains 1->None
    perform_test(1, 1, [1])
    # list initially contains 1->2->3->4->5
    perform_test(5, 1, [5, 1, 2, 3, 4])
    perform_test(5, 2, [4, 5, 1, 2, 3])
    perform_test(5, 4, [2, 3, 4, 5, 1])
    perform_test(5, 5, [1, 2, 3, 4, 5])

    print("Test passed")
