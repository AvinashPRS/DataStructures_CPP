"""
Interleave two linked lists.
eg: 1->2->3 and 101->102->103->104  ==>  1->101->2->102->3->103->104

Input: heads of the two lists
Output: head of the interleaved list

TC: O(min(m, n))
SC: O(1)
"""
import random
import sys

MAX_NUM_ELEMENTS = 10
MAX_NUM_LOOPS = 10


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def handle_error():
    print("Test failed")
    sys.exit(1)


def interleave_lists(n1, n2):
    """n1: head of the first linked list
    n2: head of the second linked list
    Returns head of the resulting interleaved linked list"""
    if n1 is None:
        return n2  # if linked list1 is empty, return n2
    if n2 is None:
        return n1  # if linked list2 is empty, return n1

    result = n1
    while n1 and n2:
        temp1 = n1.next
        temp2 = n2.next

        # place node of second linked list next to the node of the first linked list
        if n1.next:
            n2.next = n1.next
        n1.next = n2

        n1 = temp1
        n2 = temp2

    return result


def construct_list(values):
    """Constructs a linked list with the elements of values in the same order"""
    head = None
    for value in reversed(values):
        head = Node(value, head)
    return head


def print_list(head):
    cur_node = head
    while cur_node:
        print(cur_node.data, end=" ")
        cur_node = cur_node.next
    print()


def test_interleave():
    num_elems1 = random.randrange(MAX_NUM_ELEMENTS)
    num_elems2 = random.randrange(MAX_NUM_ELEMENTS)

    # if num_elems1 = 5, list1 will contain 1->2->3->4->5
    # if num_elems2 = 5, list2 will contain 101->102->103->104->105
    list1 = construct_list([i + 1 for i in range(num_elems1)])
    list2 = construct_list([101 + i for i in range(num_elems2)])

    print("Input 1: ", end="")
    print_list(list1)

    print("Input 2: ", end="")
    print_list(list2)

    result_list = interleave_lists(list1, list2)

    # verify the result
    i = 0
    cur_node = result_list
    while cur_node:
        # if index is even, then the element should be less than 100
        if i % 2 == 0 and i < 2 * num_elems1 and cur_node.data >= 100:
            handle_error()

        # if index is odd, then the element should be more than 100
        if i % 2 == 1 and i < 2 * num_elems2 and cur_node.data < 100:
            handle_error()

        i += 1
        cur_node = cur_node.next

    if i != num_elems1 + num_elems2:
        handle_error()

    print("Output : ", end="")
    print_list(result_list)

    print("__________________________________________________")


if __name__ == "__main__":
    for _ in range(MAX_NUM_LOOPS):
        test_interleave()

    print("Test passed")
