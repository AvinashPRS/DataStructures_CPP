"""
Sort a linked list using insertion sort, O(n^2).

Input: head of list
Output: head of sorted list

Solution:
    Traverse the list; whenever an element is smaller than its previous one, move it
    back into the (already sorted) prefix at its correct position, then continue the
    traversal from where we left off.

    TC: O(n^2)
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


def insertion_sort_linked_list(head):
    # 0 or 1 node: already sorted
    # (the C++ original returned nullptr here, which lost single-node lists)
    if head is None or head.next is None:
        return head

    dummy_head = create_node(float("-inf"))
    dummy_head.next = head

    # current node being traversed
    curr = head

    while curr and curr.next:
        # if current data is greater than next, move next to its correct position
        if curr.data > curr.next.data:
            unsorted_data = curr.next
            nextptr = unsorted_data.next
            # the list before current is sorted: find the first element greater than it
            prev = dummy_head
            while prev.next.data < unsorted_data.data:
                prev = prev.next
            # place unsorted_data just before the first bigger element
            unsorted_data.next = prev.next
            prev.next = unsorted_data
            # unlink it from its old position
            curr.next = nextptr
        else:
            # traverse further only when nothing was moved
            # (the C++ original advanced unconditionally, which can skip a node)
            curr = curr.next

    return dummy_head.next


if __name__ == "__main__":
    head = create_node(1)
    head.next = create_node(-2)
    head.next.next = create_node(6)
    head.next.next.next = create_node(51)
    head.next.next.next.next = create_node(2)

    head = insertion_sort_linked_list(head)
    show_list(head)
