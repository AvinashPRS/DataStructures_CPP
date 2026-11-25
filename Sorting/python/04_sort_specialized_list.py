"""Sort a linked list whose nodes contain only a few distinct values (0, 1, 2)."""
import random
import sys

MAX_NUM_ELEMENTS = 10
MAX_NUM_LOOPS = 10
MAX_VALUE = 3


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def handle_error():
    print("Test failed")
    sys.exit(1)


def add_node(head, tail, cur_node, i):
    """
    head: list of head references of the separated lists
    tail: list of tail references of the separated lists
    cur_node: current node being processed
    i: data value of the node
    """
    cur_node.next = head[i]
    head[i] = cur_node
    if tail[i] is None:
        tail[i] = cur_node


def sort_list(first_node, num_distinct_values):
    """
    first_node: first node in list to be sorted
    num_distinct_values: number of distinct values in the nodes
    Return value: head of the sorted list
    """
    if first_node is None:
        return None

    head = [None] * num_distinct_values
    tail = [None] * num_distinct_values

    # Partition the list into separate lists (0-list, 1-list, 2-list)
    cur_node = first_node
    while cur_node:
        next_node = cur_node.next
        add_node(head, tail, cur_node, cur_node.data)
        cur_node = next_node

    # Connect the tail of first linked list with head of second linked list and so on
    result = head[0]
    last_element = tail[0]
    for i in range(1, num_distinct_values):
        if result is None:
            result = head[i]

        # Link last element of previous list with head of current list
        if last_element:
            last_element.next = head[i]

        # Update the last element to the tail of current list
        if tail[i]:
            last_element = tail[i]

    return result


def construct_list(num_elements):
    head = None
    for _ in range(num_elements):
        head = Node(random.randrange(MAX_VALUE), head)
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
    list1 = construct_list(num_elems1)

    print("Input  : ", end="")
    print_list(list1)

    list1 = sort_list(list1, MAX_VALUE)

    print("Output : ", end="")
    print_list(list1)

    verify_list(list1)
    print("__________________________________________________")


if __name__ == "__main__":
    for _ in range(MAX_NUM_LOOPS):
        test()
    print("Test passed")
