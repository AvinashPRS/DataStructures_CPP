"""
Problem:
    Given two sorted linked lists in ascending order, merge the two lists
    into one single sorted list in place

Input:
    head1: head of list 1
    head2: head of list 2

Output:
    head: head of merged list

TC: O(n+m), n and m: length of list1 and list2
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


def merge_sorted_lists(head1, head2):
    """Merges two sorted linked lists (without a dummy node)."""
    # check if any of the lists is empty or not
    if head1 is None or head2 is None:
        return head1 if head1 else head2

    # link the first node of the merged list
    if head1.data < head2.data:
        head = head1
        head1 = head1.next
    else:
        head = head2
        head2 = head2.next
    rear = head

    # compare the nodes from the two lists and add the smaller one
    # to the end of the merged list
    while head1 and head2:
        if head1.data <= head2.data:
            rear.next = head1
            head1 = head1.next
        else:
            rear.next = head2
            head2 = head2.next
        rear = rear.next

    # add the remaining elements to the final list
    rear.next = head1 if head1 else head2

    return head


if __name__ == "__main__":
    head1 = Node(1)
    for pos, val in enumerate([3, 8, 12, 13], start=1):
        head1 = insert_node(head1, val, pos)
    display_nodes(head1)

    head2 = Node(2)
    for pos, val in enumerate([3, 4, 9, 16, 19], start=1):
        head2 = insert_node(head2, val, pos)
    display_nodes(head2)

    head = merge_sorted_lists(head1, head2)
    display_nodes(head)
