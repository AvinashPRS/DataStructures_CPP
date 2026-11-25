"""
Problem:
    Given a positive integer 'k' and a linked list, reverse 'k' nodes
    at a time. Leftover nodes (fewer than k) at the end are kept as is.
    eg: 1,2,3,4,5,6,7,8,9 and k = 3
        3,2,1,6,5,4,9,8,7

Input:
    k: integer
    head of the linked list

Output:
    head of linked list after reversal

TC: O(n)
SC: O(1)
"""


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def insert_node(head, data, pos):
    """Inserts a node at the given (0-indexed) position. Returns the head."""
    if head is None or pos == 0:
        return Node(data, head)

    temp = head
    curr_pos = 0
    while temp and curr_pos < pos - 1:
        curr_pos += 1
        temp = temp.next

    if temp:
        temp.next = Node(data, temp.next)
    else:
        print("Position is much farther than the length of the list")
    return head


def display_nodes(head):
    while head:
        print(head.data, end="-->")
        head = head.next
    print("NULL\n")


def reverse_list_iter(head):
    """Reverses the list iteratively. TC: O(n)"""
    prev = None
    while head:
        next_node = head.next
        head.next = prev
        prev = head
        head = next_node
    return prev


def reverse_k_nodes(head, k):
    """Reverses the list k nodes at a time."""
    if head is None or k <= 1:
        return head

    dummy = Node(0, head)
    prev = dummy  # last node of the previously processed group

    while True:
        # check that k nodes are available starting from prev.next
        start = prev.next
        last = start
        count = 1
        while last and count < k:
            last = last.next
            count += 1

        # fewer than k nodes left, keep them as they are
        if last is None:
            break

        # detach the group, reverse it and join it back
        rest = last.next
        last.next = None
        prev.next = reverse_list_iter(start)
        start.next = rest  # start is now the last node of the reversed group
        prev = start

    return dummy.next


if __name__ == "__main__":
    head1 = Node(10)
    for i in range(9, -1, -1):
        head1 = insert_node(head1, i, 0)
    display_nodes(head1)

    head = reverse_k_nodes(head1, 3)
    display_nodes(head)
