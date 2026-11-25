"""
Find the kth node from the end of a linked list.

Input: head of the list, k (k starts from 1)
Output: kth node from end if it exists, None otherwise

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


def find_kth_node_from_end(head, k):
    """head: first node of the linked list
    k: node position from the end. k starts from 1 onwards
    Returns kth node from end if it exists, None otherwise"""
    length = 0
    n1 = head
    while n1:
        length += 1
        n1 = n1.next

    n1 = head
    for i in range(1, length + 1):
        # check if the current node is the kth node from end
        if i == length - k + 1:
            return n1
        n1 = n1.next

    # k value passed doesn't match with the linked list
    return None


def construct_list(num_elements):
    """If num_elements = 2, the list will be 1->2"""
    head = None
    for value in range(num_elements, 0, -1):
        head = Node(value, head)
    return head


def print_list(head):
    cur_node = head
    while cur_node:
        print(cur_node.data, end=" ")
        cur_node = cur_node.next
    print()


if __name__ == "__main__":
    # test for different list lengths ranging from 1 to MAX_NUM_ELEMENTS_IN_LIST
    for num_elems in range(1, MAX_NUM_ELEMENTS_IN_LIST + 1):
        head = construct_list(num_elems)

        # test for different k values ranging from 0 to num_elems + 1
        for k in range(num_elems + 2):
            print("Input  : ", end="")
            print_list(head)

            # find the kth node from the end
            k_node = find_kth_node_from_end(head, k)

            print(f"Size = {num_elems}, {k}th node from end is ", end="")
            print(f"{k_node.data} " if k_node else "Empty")

            # verify the kth node from the end
            if 1 <= k <= num_elems:
                if k_node.data != num_elems - k + 1:
                    handle_error()
            elif k_node is not None:
                handle_error()

            print("____________________________________________________")

    print("Test passed")
