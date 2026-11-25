"""
Problem:
    Given a linked list, reverse the nodes

Input:
    head of the list

Output:
    reversed list head

TC: O(n)
SC: O(1) iterative, O(n) recursive (call stack)
"""


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def insert_node(head, data, pos):
    """Inserts a node at the given (0-indexed) position. Returns the head."""
    if head is None or pos == 0:
        print(f"Node {data} added")
        return Node(data, head)

    temp = head
    curr_pos = 0
    while temp and curr_pos < pos - 1:
        curr_pos += 1
        temp = temp.next

    if temp:
        temp.next = Node(data, temp.next)
        print(f"Node {data} added")
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
        next_node = head.next  # next node
        head.next = prev  # reverse the current node
        prev = head  # store the current node
        head = next_node
    return prev


def reverse_list_recur(head):
    """Reverses the list recursively.
    At each node we make the next node point to the current node."""
    # if this is the last node or None
    if head is None or head.next is None:
        return head

    next_node = head.next
    # recurse further
    rev_head = reverse_list_recur(next_node)
    # make the next node point to the current node
    next_node.next = head
    # make the current node point to None
    head.next = None

    return rev_head


def build_list():
    head = Node(1)
    for pos, val in enumerate([3, 8, 12, 13], start=1):
        head = insert_node(head, val, pos)
    return head


if __name__ == "__main__":
    head1 = build_list()
    display_nodes(head1)
    display_nodes(reverse_list_iter(head1))

    head1 = build_list()
    display_nodes(head1)
    display_nodes(reverse_list_recur(head1))
