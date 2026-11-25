"""
Reversing a singly linked list (https://simple.wikipedia.org/wiki/Linked_list)

Values are appended by walking to the last link. The list is reversed using
three pointers - current, previous and next_node: save curr.next, point
curr.next at prev, then advance prev and curr. Finally head = prev.
"""
import copy
import sys


class Node:
    def __init__(self, val=0, nxt=None):
        self.val = val    # value of the current link
        self.next = nxt   # next link in the list


def copy_all_nodes(node):
    """Deep copy of the list starting at node."""
    head = tail = None
    while node:
        new = Node(node.val)
        if head is None:
            head = tail = new
        else:
            tail.next = new
            tail = new
        node = node.next
    return head


class LinkedList:
    def __init__(self, other=None):
        # copy constructor creates a deep copy of every node
        self.head = copy_all_nodes(other.head) if other else None

    def __copy__(self):
        return LinkedList(self)

    def is_empty(self):
        return self.head is None

    def insert(self, n):
        """Add a new element at the end of the list."""
        new_node = Node(n)
        if self.is_empty():
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node

    def reverse_list(self):
        curr, prev = self.head, None
        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self.head = prev

    def display(self):
        out, t = [], self.head
        while t:
            out.append(str(t.val))
            t = t.next
        print(" ".join(out))

    def top(self):
        if self.is_empty():
            raise ValueError("List is empty")
        return self.head.val

    def last(self):
        if self.is_empty():
            raise ValueError("List is empty")
        t = self.head
        while t.next is not None:
            t = t.next
        return t.val

    def traverse(self, index):
        current, count = self.head, 0
        while current is not None:
            if count == index:
                return current.val
            count += 1
            current = current.next
        # caller asked for a non-existent element
        sys.exit(1)


def test():
    L = LinkedList()
    for v in (11, 12, 15, 10, -12, -20, 18):
        L.insert(v)
    assert L.top() == 11
    assert L.last() == 18
    L.reverse_list()
    # Reversal testing
    assert L.top() == 18
    assert L.traverse(1) == -20
    assert L.traverse(2) == -12
    assert L.traverse(3) == 10
    assert L.traverse(4) == 15
    assert L.traverse(5) == 12
    assert L.last() == 11
    print("All tests have successfully passed!")


def _check_copies(L, other):
    other.insert(40)
    L.insert(400)
    assert L.top() == 10 and other.top() == 10
    assert L.traverse(1) == 20 and other.traverse(1) == 20
    assert L.traverse(2) == 30 and other.traverse(2) == 30
    assert L.last() == 400
    assert other.last() == 40


def test_copy_constructor():
    L = LinkedList()
    for v in (10, 20, 30):
        L.insert(v)
    _check_copies(L, LinkedList(L))


def test_assignment_operator():
    L = LinkedList()
    for v in (10, 20, 30):
        L.insert(v)
    other = copy.copy(L)  # deep copy of the nodes (like operator=)
    _check_copies(L, other)


def main():
    test()
    test_copy_constructor()
    test_assignment_operator()


if __name__ == "__main__":
    main()
