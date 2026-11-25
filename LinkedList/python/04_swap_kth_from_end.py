"""
Swap the kth node from the beginning with the kth node from the end of a
linked list (by relinking nodes, not by swapping data).

Input: head of the list, k, length of the list
Output: head of the resulting list, None on error

TC: O(n)
SC: O(1)
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


def construct_list(num_elements):
    """If num_elements = 2, the list will be 1->2"""
    head = None
    for value in range(num_elements, 0, -1):
        head = Node(value, head)
    return head


def find_kth_node_from_begin(head, k):
    """Returns (kth node from beginning, node previous to it).
    Returns (None, None) if the kth node doesn't exist."""
    cur_node = head
    prev = None
    i = 1
    while cur_node:
        if i == k:
            return cur_node, prev
        prev = cur_node
        cur_node = cur_node.next
        i += 1
    return None, None


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

    # k value passed doesn't match with the linked list
    return None, None


def swap_neighbors(head, prev, n1, n2):
    """Helper function which swaps two neighbors n1 and n2.
    prev: node previous to n1
    n2 occurs immediately after n1
    Returns head of the resulting list after swapping neighbors"""
    n1.next = n2.next
    n2.next = n1

    if prev:
        prev.next = n2
    else:
        head = n2  # if prev doesn't exist, update head to n2
    return head


def swap_kth_node(head, k, length):
    """Main function for swapping the kth node from beginning and end.
    Returns head of the resulting list on success, None on error"""
    if head is None or k < 1 or k > length:
        return None

    # k1 is the kth node from beginning and prev1 is previous to k1
    k1, prev1 = find_kth_node_from_begin(head, k)

    # k2 is the kth node from end and prev2 is previous to k2
    k2, prev2 = find_kth_node_from_end(head, k, length)

    if k1 is None or k2 is None:
        return None  # the k value is incorrect

    if k1 is k2:
        return head  # both nodes are the same, so no need to swap

    # handle the case where k1 and k2 are neighbors
    if k1.next is k2:
        return swap_neighbors(head, prev1, k1, k2)

    if k2.next is k1:
        return swap_neighbors(head, prev2, k2, k1)

    # k1 and k2 are not neighbors. So swap k1.next with k2.next
    k1.next, k2.next = k2.next, k1.next

    if prev1:
        prev1.next = k2
    else:
        head = k2  # after swap, k2 becomes new head

    if prev2:
        prev2.next = k1
    else:
        head = k1  # after swap, k1 becomes new head

    return head


if __name__ == "__main__":
    # test for different list lengths
    for num_elems in range(MAX_NUM_ELEMENTS_IN_LIST + 1):
        head = construct_list(num_elems)

        # passing k value of 0 should result in an error
        if swap_kth_node(head, 0, num_elems) is not None:
            handle_error()

        # test for different k values
        for k in range(1, num_elems + 1):
            print(f"Size = {num_elems}, k = {k} ")
            print("Input  : ", end="")
            print_list(head)

            # swap the kth element
            head = swap_kth_node(head, k, num_elems)

            print("Output : ", end="")
            print_list(head)

            # verify the result
            k_node, _ = find_kth_node_from_begin(head, k)
            if k_node.data != num_elems - k + 1:
                handle_error()

            # again swap the kth element to get back the original list
            head = swap_kth_node(head, num_elems - k + 1, num_elems)

            # verify the result
            k_node, _ = find_kth_node_from_begin(head, k)
            if k_node.data != k:
                handle_error()

            print("_______________________________________")

        # passing a value of k greater than the length of list should return an error
        if swap_kth_node(head, num_elems + 1, num_elems) is not None:
            handle_error()

    print("Test passed")
