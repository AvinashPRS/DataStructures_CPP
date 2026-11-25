# Exercise 11-8: a doubly linked list with a bidirectional iterator.


class Node:
    def __init__(self, value=0):
        self.value = value
        self.next = None
        self.prev = None


class NodeItr:
    def __init__(self, node):
        self._node = node

    def inc(self):
        self._node = self._node.next
        return self

    def dec(self):
        self._node = self._node.prev
        return self

    def get(self):
        return self._node.value

    def __eq__(self, other):
        return self._node is other._node

    def __ne__(self, other):
        return not self == other


class Lis:
    def __init__(self, n=0, value=0, iterable=None):
        self._b = self._e = None
        self._s = 0
        if iterable is not None:
            for v in iterable:
                self.push_back(v)
        else:
            for _ in range(n):
                self.push_back(value)

    def push_back(self, value):
        node = Node(value)
        if self._s == 0:
            self._b = self._e = node
        else:
            self._e.next = node
            node.prev = self._e
            self._e = node
        self._s += 1

    def size(self):
        return self._s

    def empty(self):
        return self._s == 0

    def clear(self):
        self._b = self._e = None
        self._s = 0

    def begin(self):
        return NodeItr(self._b)

    def end(self):
        return NodeItr(None)

    def __iter__(self):
        node = self._b
        while node is not None:
            yield node.value
            node = node.next
