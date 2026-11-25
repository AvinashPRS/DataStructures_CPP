"""
Problem:
    Given a linked list and a range 'a' and 'b' (1-indexed), reverse the
    nodes in the range [a, b].
    eg: 0->1->2->3->4->5, a = 2, b = 4  ==>  0->3->2->1->4->5

Input:
    head of the list
    a: int
    b: int

Output:
    head of the transformed list

TC: O(n)
SC: O(1)
"""


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def insert_node(head, data, pos):
    """Inserts a node at the given (0-indexed) position.
    Returns the (possibly new) head. TC: O(n)"""
    # if the list is empty or the node is to be inserted at the front
    if head is None or pos == 0:
        return Node(data, head)

    # traverse till the node before the required position
    temp = head
    curr_pos = 0
    while temp and curr_pos < pos - 1:
        curr_pos += 1
        temp = temp.next

    # if the position is farther than the current length + 1, show error
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


def reverse_sublist(head, a, b):
    """Reverses the nodes in positions [a, b] (1-indexed) and returns the head."""
    if head is None or a >= b:
        return head

    # a dummy node before head handles the case where a == 1
    dummy = Node(0, head)

    # find the node just before the ath node
    start_prev = dummy
    for _ in range(a - 1):
        start_prev = start_prev.next
        if start_prev is None:
            return head  # a is beyond the length of the list

    # ath node will become the last node of the reversed sublist
    ath_node = start_prev.next

    # find the bth node (or the last node if b is beyond the list)
    bth_node = ath_node
    count = a
    while bth_node and bth_node.next and count < b:
        bth_node = bth_node.next
        count += 1
    if bth_node is None:
        return head

    # detach the sublist, reverse it and connect it back
    rest = bth_node.next
    bth_node.next = None
    start_prev.next = reverse_list_iter(ath_node)
    ath_node.next = rest

    return dummy.next


if __name__ == "__main__":
    head1 = Node(10)
    for i in range(9, -1, -1):
        head1 = insert_node(head1, i, 0)
    display_nodes(head1)

    new_head = reverse_sublist(head1, 3, 10)
    display_nodes(new_head)
