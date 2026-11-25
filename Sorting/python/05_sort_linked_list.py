"""Merge sort a singly linked list (length known in advance)."""
import random
import sys

MAX_NUM_ELEMENTS = 10
MAX_NUM_LOOPS = 10
MAX_VALUE = 100


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def handle_error():
    print("Test failed")
    sys.exit(1)


def merge_lists(n1, n2):
    """
    n1 - head of first sorted list
    n2 - head of second sorted list
    Result - head of merged sorted list
    """
    if n1 is None:
        return n2
    if n2 is None:
        return n1

    # Since we are sorting in ascending order, result points to the smaller node
    if n1.data <= n2.data:
        result = n1
        n1 = n1.next
    else:
        result = n2
        n2 = n2.next

    # Process the two lists
    merge_node = result
    while n1 is not None and n2 is not None:
        if n1.data <= n2.data:
            merge_node.next = n1
            n1 = n1.next
        else:
            merge_node.next = n2
            n2 = n2.next
        merge_node = merge_node.next

    # Append whichever list still has nodes
    merge_node.next = n1 if n1 else n2

    return result


def sort_list(first_node, num_elements):
    """
    first_node: head of the list to be sorted
    num_elements: number of elements in the list
    Return value: head of the merged and sorted list
    """
    if num_elements == 0:
        return None

    # A single node: disconnect next and return it
    if num_elements == 1:
        first_node.next = None
        return first_node

    # Divide the list into two lists of count1 and count2 elements
    list1 = first_node
    count1 = num_elements // 2

    cur_node = first_node
    for _ in range(count1):
        cur_node = cur_node.next

    list2 = cur_node
    count2 = num_elements - count1

    # Sort recursively, then merge
    list1 = sort_list(list1, count1)
    list2 = sort_list(list2, count2)
    return merge_lists(list1, list2)


def construct_list(num_elements, max_value):
    head = None
    for _ in range(num_elements):
        head = Node(random.randrange(max_value), head)
    return head


def verify_list(head):
    prev_node = None
    cur_node = head
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


def test():
    num_elems1 = random.randrange(MAX_NUM_ELEMENTS)
    list1 = construct_list(num_elems1, MAX_VALUE)

    print("Input  : ", end="")
    print_list(list1)

    list1 = sort_list(list1, num_elems1)

    print("Output : ", end="")
    print_list(list1)

    verify_list(list1)
    print("__________________________________________________")


if __name__ == "__main__":
    for _ in range(MAX_NUM_LOOPS):
        test()
    print("Test passed")
