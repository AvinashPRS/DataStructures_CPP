"""
    Design a Binary Search Tree class.
    Solution:
        TC: Insertion: Avg: O(logn), worst: O(n) when skewed
            Deletion:  Avg: O(logn), worst: O(n) when skewed
            Lookup:    Avg: O(logn), worst: O(n) when skewed
        SC: O(1) extra for insert/delete (iterative), O(h) for the traversal
"""


class BinarySearchTree:
    class Node:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        self.root_ = None

    def insert(self, key):
        """Walk down comparing key with each node until an empty spot is found
        and link a new node there. Returns False if key already exists."""
        if self.root_ is None:
            self.root_ = self.Node(key)
            return True
        curr, parent = self.root_, None
        while curr:
            parent = curr
            if curr.data == key:
                return False
            curr = curr.right if curr.data < key else curr.left
        if key > parent.data:
            parent.right = self.Node(key)
        else:
            parent.left = self.Node(key)
        return True

    def _replace_child(self, parent, child, new_child):
        if parent is None:          # deleting the root
            self.root_ = new_child
        elif parent.left is child:
            parent.left = new_child
        else:
            parent.right = new_child

    def delete(self, key):
        """
        Find the key; if not found return False, else:
          - leaf: unlink it from its parent
          - one child: link the parent to that child instead
          - two children: copy the successor (leftmost node of right subtree)
            into the node and unlink the successor (it has no left child)
        """
        if self.root_ is None:
            return False
        curr, parent = self.root_, None
        while curr and curr.data != key:
            parent = curr
            curr = curr.left if curr.data > key else curr.right
        if curr is None:
            return False

        if curr.left and curr.right:
            successor, successor_parent = curr.right, None
            while successor.left:
                successor_parent = successor
                successor = successor.left
            curr.data = successor.data
            if successor_parent is None:   # right child has no left child
                curr.right = successor.right
            else:                          # successor may have a right subtree
                successor_parent.left = successor.right
        elif curr.left:
            self._replace_child(parent, curr, curr.left)
        elif curr.right:
            self._replace_child(parent, curr, curr.right)
        else:
            self._replace_child(parent, curr, None)
        return True

    def in_order_traversal(self, it):
        if it:
            self.in_order_traversal(it.left)
            print(it.data, end=" ")
            self.in_order_traversal(it.right)

    def get_root(self):
        return self.root_


def main():
    bst = BinarySearchTree()
    for v in (5, 2, 6, 7, 3, 1):
        bst.insert(v)
    bst.in_order_traversal(bst.get_root())
    print()
    bst.delete(5)
    bst.in_order_traversal(bst.get_root())
    print()


if __name__ == "__main__":
    main()
