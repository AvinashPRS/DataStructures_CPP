"""
Find the first common (intersection) node of two linked lists.

Approach: find the lengths of both lists, advance the longer one by the
difference, then walk both together until the nodes match.

TC: O(m + n)
SC: O(1)
"""
import random
import sys

MAX_NUM_ELEMS = 10
MAX_NUM_TESTS = 10


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def handle_error():
    print("Test failed")
    sys.exit(1)


def construct_list(num_elements, start_value):
    """If num_elements = 2 and start_value = 100, the list is 100->101"""
    head = None
    for value in range(start_value + num_elements - 1, start_value - 1, -1):
        head = Node(value, head)
    return head


def print_list(head):
    cur_node = head
    while cur_node:
        print(cur_node.data, end=" ")
        cur_node = cur_node.next
    print()


def find_length(n1):
    length = 0
    while n1:
        n1 = n1.next
        length += 1
    return length


def find_intersection_node(head1, head2):
    """Returns the first common node between the two linked lists, or None."""
    # find the length of the two linked lists
    length1 = find_length(head1)
    length2 = find_length(head2)

    # store head of the longer list in n1 and head of the shorter list in n2
    if length1 >= length2:
        n1, n2 = head1, head2
    else:
        n1, n2 = head2, head1

    # advance n1 by the difference in length of the two lists
    for _ in range(abs(length1 - length2)):
        n1 = n1.next

    # go on comparing the nodes till n1 and n2 match
    while n1 and n2 and n1 is not n2:
        n1 = n1.next
        n2 = n2.next

    # n1 will have the common node if it exists, otherwise n1 will be None
    return n1


def get_last_node(head):
    n = head
    while n and n.next:
        n = n.next
    return n


def test():
    # randomly generate three lists:
    # list1: 0->1->..., list2: 100->101->..., list3: 200->201->...
    head1 = construct_list(random.randrange(MAX_NUM_ELEMS), 0)
    head2 = construct_list(random.randrange(MAX_NUM_ELEMS), 100)
    head3 = construct_list(random.randrange(MAX_NUM_ELEMS), 200)

    n1 = get_last_node(head1)
    n2 = get_last_node(head2)

    # connect the last element of list1 and list2 to the first element of list3
    if n1:
        n1.next = head3
    if n2:
        n2.next = head3

    print("List 1 : ", end="")
    print_list(head1)

    print("List 2 : ", end="")
    print_list(head2)

    # find the first common node between list1 and list2
    result = find_intersection_node(head1, head2)

    if result:
        print(f"Intersection node = {result.data}")
    else:
        print("No intersection node")

    # the expected result is the first element in list3
    expected_result = head3 if (n1 and n2) else None

    if result is not expected_result:
        handle_error()

    print("________________________________________________")


if __name__ == "__main__":
    for _ in range(MAX_NUM_TESTS):
        test()

    print("Test passed ")
