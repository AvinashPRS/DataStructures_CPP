"""
Multiply two numbers represented by linked lists (most significant digit first).

Approach: reverse both lists, pre-create a result list of (m + n) zero
digits and do grade-school multiplication into it, then reverse the inputs
back and reverse the result.

TC: O(m * n)
SC: O(m + n) for the result list
"""
import random
import sys

MAX_NUM_ELEMENTS_IN_LIST = 4
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


def multiply_lists(n1, n2, count1, count2):
    """n1, n2: head of the first and second linked list
    count1, count2: num elements in first and second linked list
    Returns head of a new linked list having the result of multiplication"""
    # reverse the two input linked lists
    h1 = reverse_linked_list(n1)
    h2 = reverse_linked_list(n2)

    # pre-create the result linked list
    result_head = None
    for _ in range(count1 + count2):
        result_head = Node(0, result_head)

    # perform the multiplication
    result_start_node = result_head
    p1 = h1
    while p1:
        cur_res_node = result_start_node
        p2 = h2
        carry = 0
        while p2:
            total = p1.data * p2.data + cur_res_node.data + carry
            cur_res_node.data = total % 10
            carry = total // 10

            p2 = p2.next
            cur_res_node = cur_res_node.next

        cur_res_node.data = carry

        p1 = p1.next
        result_start_node = result_start_node.next

    # reverse back the two input linked lists
    reverse_linked_list(h1)
    reverse_linked_list(h2)

    # reverse the result linked list
    return reverse_linked_list(result_head)


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
        num_elems1 = random.randrange(MAX_NUM_ELEMENTS_IN_LIST)
        head1 = construct_list(num_elems1)

        num_elems2 = random.randrange(MAX_NUM_ELEMENTS_IN_LIST)
        head2 = construct_list(num_elems2)

        result = multiply_lists(head1, head2, num_elems1, num_elems2)

        val1 = convert_list_to_value(head1)
        val2 = convert_list_to_value(head2)
        val3 = convert_list_to_value(result)

        print(f"{val1} * {val2} = {val3}\n")

        if val3 != val1 * val2:
            handle_error()

    print("Test passed")
