"""
Merge two sorted linked lists into a single sorted linked list in place.

Input: heads of the two sorted lists
Output: head of the merged list

TC: O(m + n)
SC: O(1)
"""
import random
import sys

MAX_NUM_ELEMENTS = 10
MAX_NUM_LOOPS = 10
MAX_VALUE = 10


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def handle_error():
    print("Test failed")
    sys.exit(1)


def merge_lists(n1, n2):
    """n1: head of the first linked list
    n2: head of the second linked list
    Returns head of the merged linked list"""
    if n1 is None:
        return n2  # if linked list1 is empty, return n2
    if n2 is None:
        return n1  # if linked list2 is empty, return n1

    # make the result point to the node with the smaller value
    if n1.data <= n2.data:
        result = prev_merge_node = n1
        n1 = n1.next
    else:
        result = prev_merge_node = n2
        n2 = n2.next

    # process the two linked lists
    while n1 and n2:
        if n1.data <= n2.data:
            prev_merge_node.next = n1
            n1 = n1.next
        else:
            prev_merge_node.next = n2
            n2 = n2.next
        prev_merge_node = prev_merge_node.next

    # if there are still nodes present in linked list1 or linked list2,
    # then append them to the result list
    prev_merge_node.next = n1 if n1 else n2

    return result


def construct_list(values):
    """Constructs a linked list with the elements of values in the same order"""
    head = None
    for value in reversed(values):
        head = Node(value, head)
    return head


def verify_list(head):
    """Flags an error if the elements are not in ascending order."""
    cur_node = head
    prev_node = None
    while cur_node:
        if prev_node and cur_node.data < prev_node.data:
            handle_error()
        prev_node = cur_node
        cur_node = cur_node.next


def print_list(head):
    cur_node = head
    while cur_node:
        print(cur_node.data, end=" ")
        cur_node = cur_node.next
    print()


def test_merge_sort():
    # randomly decide the size of the lists and their (sorted) contents
    array1 = sorted(random.randrange(MAX_VALUE) for _ in range(random.randrange(MAX_NUM_ELEMENTS)))
    array2 = sorted(random.randrange(MAX_VALUE) for _ in range(random.randrange(MAX_NUM_ELEMENTS)))

    # construct the lists. They will contain the elements in ascending order
    list1 = construct_list(array1)
    list2 = construct_list(array2)

    print("Input1 : ", end="")
    print_list(list1)

    print("Input2 : ", end="")
    print_list(list2)

    merged_list = merge_lists(list1, list2)

    print("Output : ", end="")
    print_list(merged_list)

    verify_list(merged_list)

    print("__________________________________________")


if __name__ == "__main__":
    for _ in range(MAX_NUM_LOOPS):
        test_merge_sort()

    print("Test passed")
