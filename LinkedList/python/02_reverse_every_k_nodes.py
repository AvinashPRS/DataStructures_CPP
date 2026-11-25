"""
Reverse every k nodes of a linked list.
eg: 1->2->3->4->5, k = 2  ==>  2->1->4->3->5

Input: head of the list, k
Output: head of the new list after reversing every k nodes

TC: O(n)
SC: O(n/k) for the recursion
"""
MAX_NUM_ELEMENTS_IN_LIST = 10


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def k_reverse_list(head, k):
    """head: first node of the linked list
    k: how many nodes should be reversed
    Returns first node of the new linked list after reversing every k nodes"""
    if head is None or k == 0:
        return head

    cur_node = head
    prev_node = None
    i = 0

    while cur_node and i < k:
        # store the next node in a temporary variable
        temp_node = cur_node.next
        # reverse the link
        cur_node.next = prev_node
        # update the previous node to the current node
        prev_node = cur_node
        # proceed to the next node in the original linked list
        cur_node = temp_node
        i += 1

    # We have reversed k nodes. cur_node points to the (k+1)th node and head
    # points to the kth node. Now recursively process the remaining nodes from
    # cur_node onwards and assign the result to head.next
    if cur_node:
        head.next = k_reverse_list(cur_node, k)

    # prev_node will point to first node in linked list after reversal
    return prev_node


def print_list(head):
    cur_node = head
    while cur_node:
        print(cur_node.data, end=" ")
        cur_node = cur_node.next


def construct_list(num_elements):
    """If num_elements = 2, the list will be 1->2"""
    head = None
    for value in range(num_elements, 0, -1):
        head = Node(value, head)
    return head


def test_01():
    # test for different list lengths ranging from 0 to MAX_NUM_ELEMENTS_IN_LIST
    for num_elems in range(MAX_NUM_ELEMENTS_IN_LIST + 1):
        # test for different k values ranging from 0 to MAX_NUM_ELEMENTS_IN_LIST + 1
        for k in range(MAX_NUM_ELEMENTS_IN_LIST + 2):
            head = construct_list(num_elems)

            print(f"Size = {num_elems}, K = {k}")

            print("Original: ", end="")
            print_list(head)
            print()

            head = k_reverse_list(head, k)

            print("Reversed: ", end="")
            print_list(head)
            print()

            print("_________________________________________")

    print("Test passed")


if __name__ == "__main__":
    test_01()
