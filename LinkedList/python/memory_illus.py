"""
Memory illustration for linked list nodes.

The C version demonstrates malloc / calloc / realloc for allocating nodes.
Python has no manual memory management: objects are allocated by the
interpreter when created and freed automatically (reference counting plus a
cycle-detecting garbage collector) when nothing refers to them any more.

This file shows the Python equivalents of the three C cases:
    1. "malloc"  -> create a node and explicitly initialise every field
    2. "calloc"  -> create a node with zero/None default field values
    3. "realloc" -> there is no resizing of objects; you just create a new
                    object (or, for containers, they grow on their own)
It also shows how much memory a node takes and that unreferenced nodes are
reclaimed automatically.
"""
import gc
import random
import sys
import weakref

MAX_NUM_ELEMENTS_IN_LIST = 10
MAX_VALUE = 10


class Node:
    # __slots__ avoids a per-instance __dict__, making each node smaller,
    # which is closer to a C struct with fixed fields
    __slots__ = ("data", "next", "__weakref__")

    def __init__(self, data=0, next=None):
        # like calloc: fields get zero / None defaults
        self.data = data
        self.next = next


def construct_list(num_elements):
    """Constructs a linked list with num_elements nodes. Each node's data is a
    random value between 0 and MAX_VALUE-1. The three ways of creating a node
    are used in a round-robin fashion, mirroring the C version."""
    head = None

    for i in range(num_elements):
        if i % 3 == 0:
            # CASE 1: "malloc" - create the object and explicitly set all fields
            new_node = Node.__new__(Node)  # allocated, but fields not set yet
            new_node.data = random.randrange(MAX_VALUE)
            new_node.next = None
        elif i % 3 == 1:
            # CASE 2: "calloc" - fields come pre-initialised to 0 / None
            new_node = Node()
            new_node.data = random.randrange(MAX_VALUE)
        else:
            # CASE 3: "realloc" - Python objects can't be resized in place.
            # A list grows automatically (internally it over-allocates and
            # reallocates), so we illustrate that and then create the node.
            buf = []
            print(f"  empty list size: {sys.getsizeof(buf)} bytes", end="")
            buf.append(random.randrange(MAX_VALUE))
            print(f", after append: {sys.getsizeof(buf)} bytes")
            new_node = Node(buf[0])

        # attach the newly created node to the front of our list
        new_node.next = head
        head = new_node

    return head


def print_list(head):
    cur_node = head
    while cur_node:
        print(cur_node.data, end=" ")
        cur_node = cur_node.next
    print()


if __name__ == "__main__":
    head = construct_list(MAX_NUM_ELEMENTS_IN_LIST)
    print("List   : ", end="")
    print_list(head)

    print(f"Size of one node: {sys.getsizeof(head)} bytes")

    # there is no free(): dropping the last reference releases the nodes
    probe = weakref.ref(head)
    head = None
    gc.collect()
    print("First node freed after dropping head:", probe() is None)
