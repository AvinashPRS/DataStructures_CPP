"""
Add two numbers represented by linked lists (most significant digit first).
eg: 9->5 + 7->1  ==>  1->6->6

Approach: reverse both lists so the least significant digits come first,
add digit by digit with carry (building the result from the front, so it
ends up MS digit first), then reverse the inputs back.

TC: O(m + n)
SC: O(1) extra (apart from the result list)
"""
import random
import sys

MAX_NUM_ELEMENTS_IN_LIST = 10
MAX_NUM_TESTS = 100


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def handle_error():
    print("Test failed")
    sys.exit(1)


def reverse_linked_list(head):
    current_node = head
    previous_node = None
    while current_node:
        temp_node = current_node.next
        current_node.next = previous_node
        previous_node = current_node
        current_node = temp_node
    return previous_node


def add_lists(n1, n2):
    """n1: head of the first linked list
    n2: head of the second linked list
    Returns head of a new linked list having the sum of the two lists"""
    # reverse the two input linked lists
    h1 = p1 = reverse_linked_list(n1)
    h2 = p2 = reverse_linked_list(n2)

    # add the nodes of the two linked lists
    carry = 0
    result_node = None
    while p1 and p2:
        total = p1.data + p2.data + carry
        result_node = Node(total % 10, result_node)
        carry = total // 10
        p1 = p1.next
        p2 = p2.next

    # if one of the input lists still has nodes, make p1 point to it
    if p2:
        p1 = p2

    # process the remaining input linked list
    while p1:
        total = p1.data + carry
        result_node = Node(total % 10, result_node)
        carry = total // 10
        p1 = p1.next

    # if carry is non-zero, then store the carry in the result linked list
    if carry:
        result_node = Node(carry, result_node)

    # reverse back the two input linked lists
    reverse_linked_list(h1)
    reverse_linked_list(h2)

    # the result node already points to the MS digit,
    # so no need to reverse the result list
    return result_node


def construct_list(num_elements):
    head = None
    for _ in range(num_elements):
        head = Node(random.randrange(10), head)
    return head


def convert_list_to_value(head):
    result = 0
    cur_node = head
    while cur_node:
        result = result * 10 + cur_node.data
        cur_node = cur_node.next
    return result


if __name__ == "__main__":
    # try out several tests where the inputs are randomly generated
    for _ in range(MAX_NUM_TESTS):
        head1 = construct_list(random.randrange(MAX_NUM_ELEMENTS_IN_LIST))
        head2 = construct_list(random.randrange(MAX_NUM_ELEMENTS_IN_LIST))

        result = add_lists(head1, head2)

        val1 = convert_list_to_value(head1)
        val2 = convert_list_to_value(head2)
        val3 = convert_list_to_value(result)

        print(f"{val1} + {val2} = {val3}\n")

        if val3 != val1 + val2:
            handle_error()

    print("Test passed")
