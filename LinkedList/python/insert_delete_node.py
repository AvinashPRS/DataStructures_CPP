"""
Problem:
    Make a linked list and write functions for inserting and deleting
    nodes at any position

Input:
    head: head of list
    pos: position to perform operation, it is zero indexed

Output:
    updated list

TC: O(n) for both insertion and deletion, n: length of list
"""


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def insert_node(head, data, pos):
    """Inserts a node at the given position. Returns the (possibly new) head."""
    # if the list is empty, make the new node the head
    if head is None:
        return Node(data)

    # if the node is to be inserted at the front
    if pos == 0:
        print(f"Node {data} added")
        return Node(data, head)

    # traverse till the node before the required position
    temp = head
    curr_pos = 0
    while temp and curr_pos < pos - 1:
        curr_pos += 1
        temp = temp.next

    # if the position is farther than the current length + 1, show error
    if temp:
        # new node points to the node that was at this position and the
        # previous node points to the new node
        temp.next = Node(data, temp.next)
        print(f"Node {data} added")
    else:
        print("Position is much farther than the length of the list")
    return head


def delete_node(head, pos):
    """Deletes the node at the given position. Returns the (possibly new) head."""
    # check if the list is empty or not
    if head is None:
        print("Empty list!")
        return head

    if pos == 0:
        print("Node deleted")
        return head.next

    # traverse till the node before the target node
    temp = head
    curr_pos = 0
    while temp.next and curr_pos < pos - 1:
        curr_pos += 1
        temp = temp.next

    # check if the last node has been reached or not
    if temp.next is None or curr_pos < pos - 1:
        print("Given position out of bound")
    else:
        # make the previous node point to what the node at that position was pointing at
        temp.next = temp.next.next
        print("Node deleted")
    return head


def display_nodes(head):
    while head:
        print(head.data, end="-->")
        head = head.next
    print("NULL\n")


if __name__ == "__main__":
    head = None

    # insert nodes
    for i in range(5):
        head = insert_node(head, i, 0)
    display_nodes(head)

    # out of bound position
    head = insert_node(head, 99, 55)
    # in between pos
    head = insert_node(head, 88, 3)
    display_nodes(head)

    # last position
    head = insert_node(head, 77, 6)
    head = insert_node(head, 66, 7)
    display_nodes(head)

    # first position
    head = insert_node(head, 55, 0)
    display_nodes(head)

    # deletion
    # beginning
    head = delete_node(head, 0)
    display_nodes(head)
    # end
    head = delete_node(head, 8)
    display_nodes(head)
    # in between
    head = delete_node(head, 4)
    display_nodes(head)

    head = delete_node(head, 99)
