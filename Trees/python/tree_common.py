"""
Shared helpers used by the Interview-Druid style tree programs
(struct node, construct_bst, handle_error).
"""
import sys

MAX_NUM_NODES_IN_TREE = 10


class Node:
    """struct node - superset of the fields used by the individual programs."""

    def __init__(self, data=0, parent=None):
        self.data = data
        self.parent = parent
        self.left = None
        self.right = None
        self.depth = parent.depth + 1 if parent else 0
        self.next = None
        self.sum = 0

    def __repr__(self):
        return "Node(%r)" % (self.data,)


def construct_bst(parent, values, low, high, node_array=None):
    """Recursively construct a BST from values[low..high] (sorted ascending).
    If node_array is given, node for values[i] is stored in node_array[i]."""
    if low > high:
        return None
    middle = (low + high) // 2
    new_node = Node(values[middle], parent)
    new_node.left = construct_bst(new_node, values, low, middle - 1, node_array)
    new_node.right = construct_bst(new_node, values, middle + 1, high, node_array)
    if node_array is not None:
        node_array[middle] = new_node
    return new_node


def handle_error(msg="Test failed"):
    print(msg)
    sys.exit(1)


def check_condition(condition):
    if not condition:
        handle_error()


def is_bst(cur_node, prev_node):
    """In-order BST check. prev_node is a one-element list holding the
    in-order predecessor (the C double pointer)."""
    if cur_node is None:
        return 1
    if not is_bst(cur_node.left, prev_node):
        return 0
    if prev_node[0] is not None and cur_node.data <= prev_node[0].data:
        return 0
    prev_node[0] = cur_node
    return is_bst(cur_node.right, prev_node)


def print_list(head):
    """Print a doubly linked list made of tree nodes (next = right)."""
    out = []
    while head is not None:
        out.append("%d " % head.data)
        head = head.right
    print("".join(out) + "\n")
