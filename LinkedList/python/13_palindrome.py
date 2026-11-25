"""
Check whether a linked list (of characters) is a palindrome.

Approach: find the middle of the list using slow/fast pointers, reverse the
second half, compare it with the first half and then restore the list.

TC: O(n)
SC: O(1)
"""
import sys


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def handle_error():
    print("Test failed")
    sys.exit(1)


def reverse_linked_list(head):
    """Returns new head of the reversed list"""
    cur_node = head
    prev_node = None
    while cur_node:
        temp_node = cur_node.next
        cur_node.next = prev_node
        prev_node = cur_node
        cur_node = temp_node
    return prev_node


def is_list_palindrome(head):
    """Returns True if linked list is a palindrome, False otherwise"""
    if head is None:
        return False

    # advance p by two nodes and q by one node in each loop. So when p reaches
    # the end of linked list, q will point to the middle of the linked list
    p = q = head
    length = 0
    while p:
        length += 1
        p = p.next
        if p:
            length += 1
            p = p.next
        if p:
            q = q.next

    # reverse the second half of the linked list
    temp = r = reverse_linked_list(q.next)
    p = head

    # compare first half with reverse of second half
    is_palindrome = True
    for _ in range(length // 2):
        if p.data != r.data:
            is_palindrome = False
            break
        p = p.next
        r = r.next

    # reverse the second half again to get back the original linked list
    q.next = reverse_linked_list(temp)

    return is_palindrome


def construct_list(s):
    head = None
    for ch in reversed(s):
        head = Node(ch, head)
    return head


def print_list(head):
    cur_node = head
    while cur_node:
        print(cur_node.data, end="")
        cur_node = cur_node.next


def test(s, expected_result):
    head = construct_list(s)

    result = is_list_palindrome(head)

    print_list(head)
    if result:
        print(" ----> is palindrome ")
    else:
        print(" ----> is not palindrome ")

    if result != expected_result:
        handle_error()

    print("______________________________________")


if __name__ == "__main__":
    test("a", True)
    test("abba", True)
    test("level", True)
    test("Hello", False)

    print("Test passed")
