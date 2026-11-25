"""
Sort a linked list with merge sort: O(n log n), no extra space except the recursion stack.

Split the list in half recursively until each part has one node, then merge.

TC: O(n log n)
SC: O(1) (excluding recursion)
"""


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def create_node(data):
    return Node(data)


def show_list(head):
    while head:
        print(head.data, end=" ")
        head = head.next
    print()


def merge_linked_lists(head1, head2):
    """Merges two sorted lists using a dummy (sentinel) node."""
    dummy = Node(0)
    tail = dummy

    while head1 and head2:
        if head1.data <= head2.data:
            tail.next = head1
            head1 = head1.next
        else:
            tail.next = head2
            head2 = head2.next
        tail = tail.next

    # Attach whichever list is left over
    tail.next = head1 if head1 else head2
    return dummy.next


def find_middle_node(head):
    """Returns the last node of the first half."""
    if head is None:
        return None

    # Starting fast at head.next makes slow land at the end of the first half
    slow = head
    fast = head.next
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    return slow


def merge_sort_linked_list(head):
    # Base case: 0 or 1 node lists are already sorted
    if head is None or head.next is None:
        return head

    middle = find_middle_node(head)
    list_starting_middle = middle.next

    # Sever the link to split the list in two halves
    middle.next = None

    sorted_left = merge_sort_linked_list(head)
    sorted_right = merge_sort_linked_list(list_starting_middle)

    return merge_linked_lists(sorted_left, sorted_right)


if __name__ == "__main__":
    head = create_node(1909)
    head.next = create_node(2222)
    head.next.next = create_node(6)
    head.next.next.next = create_node(51)
    head.next.next.next.next = create_node(254)

    print("Original List:")
    show_list(head)

    sorted_head = merge_sort_linked_list(head)

    print("Sorted List:")
    show_list(sorted_head)
