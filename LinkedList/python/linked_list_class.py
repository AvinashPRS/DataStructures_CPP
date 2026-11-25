"""
Implement a Linked List class

TC:
    Insertion: When only the data is given (not the node)
                    head: O(1)
                    tail: O(1) (using the tail pointer)
                    any position : O(n)
    Deletion:  When only the data is given (not the node)
                    head: O(1)
                    any position till last : O(n)
"""


class LinkedList:
    class _Node:
        __slots__ = ("data", "next")

        def __init__(self, data, next=None):
            self.data = data
            self.next = next

    def __init__(self):
        self._head = None
        self._tail = None

    def insert_front(self, data):
        """Adds a node to the front of the list"""
        self._head = self._Node(data, self._head)
        # if the list was empty, the new node is also the tail
        if self._tail is None:
            self._tail = self._head

    def insert_back(self, data):
        """Adds a node to the back of the list"""
        # if the list is empty
        if self._head is None:
            self.insert_front(data)
            return

        # add the node using the tail pointer
        node = self._Node(data)
        self._tail.next = node
        self._tail = node

    def insert_at_position(self, data, k):
        """Adds a node at position k (1-indexed)"""
        # if the list is empty, insertion at k is not possible
        if self.empty() or k <= 0:
            return False

        # insertion at head position
        if k == 1:
            self.insert_front(data)
            return True

        # traverse the list till the (k-1)th position
        it = self._head
        pos = 1
        while it and pos < k - 1:
            it = it.next
            pos += 1

        # if the list length is lesser than k - 1, insertion not possible
        if it is None:
            print("Position greater than list length!!")
            return False

        # make the new node point to list nodes after kth pos and
        # make the (k-1)th node point to the new node
        it.next = self._Node(data, it.next)
        if it is self._tail:
            self._tail = it.next
        return True

    def delete_front(self):
        """Deletes the node at the front"""
        if self.empty():
            return False

        self._head = self._head.next
        if self._head is None:
            self._tail = None
        return True

    def delete_back(self):
        """Deletes the node at the back"""
        if self.empty():
            return False

        # only one node in the list
        if self._head is self._tail:
            self._head = self._tail = None
            return True

        # traverse till the second last node
        it = self._head
        while it.next is not self._tail:
            it = it.next

        # delete the last node
        it.next = None
        self._tail = it
        return True

    def delete_at_position(self, k):
        """Deletes the node at position k (1-indexed)"""
        if self.empty() or k <= 0:
            return False

        # deletion at head position
        if k == 1:
            return self.delete_front()

        # traverse the list till the (k-1)th position
        it = self._head
        pos = 1
        while it and pos < k - 1:
            it = it.next
            pos += 1

        # if the list length is lesser than k, deletion not possible
        if it is None or it.next is None:
            print("Position greater than list length!!")
            return False

        if it.next is self._tail:
            self._tail = it
        it.next = it.next.next
        return True

    def empty(self):
        """Checks if the list is empty or not"""
        return self._head is None

    def display(self):
        """Displays the linked list"""
        it = self._head
        while it:
            print(it.data, end=" ")
            it = it.next
        print()


if __name__ == "__main__":
    l = LinkedList()
    l.insert_front(1)
    l.insert_front(2)
    l.insert_front(3)

    l.insert_back(1)
    l.insert_back(2)

    l.display()

    l.insert_at_position(22, 3)
    l.insert_at_position(33, 7)
    l.insert_at_position(44, 1)
    print(int(l.insert_at_position(55, 99)))

    l.display()

    l.delete_front()
    l.display()

    l.delete_at_position(3)
    l.display()

    l.delete_at_position(1)
    l.display()

    l.delete_at_position(5)
    l.display()

    l.delete_back()
    l.display()
