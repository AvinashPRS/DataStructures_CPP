"""
Merge two sorted linked lists in place using a dummy node.

TC: O(n + m)
SC: O(1)
"""


class Node:
    def __init__(self, data=0, next=None):
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


def merge_sorted_lists(head1, head2):
    """Merges two sorted linked lists in-place."""
    # a temporary dummy node acts as the anchor for the starting head
    dummy = Node()
    rear = dummy

    # compare nodes from both lists and weave them together
    while head1 and head2:
        if head1.data <= head2.data:
            rear.next = head1  # link node from list 1
            head1 = head1.next  # advance list 1
        else:
            rear.next = head2  # link node from list 2
            head2 = head2.next  # advance list 2
        rear = rear.next  # advance the combined tail pointer

    # append whichever list still has elements remaining
    rear.next = head1 if head1 else head2

    # the actual head is the node following the dummy node
    return dummy.next


if __name__ == "__main__":
    head1 = Node(1)
    for pos, val in enumerate([3, 8, 12, 13], start=1):
        head1 = insert_node(head1, val, pos)
    print("List 1:")
    display_nodes(head1)

    head2 = Node(2)
    for pos, val in enumerate([3, 4, 9, 16, 19], start=1):
        head2 = insert_node(head2, val, pos)
    print("List 2:")
    display_nodes(head2)

    head = merge_sorted_lists(head1, head2)
    print("Merged List:")
    display_nodes(head)
