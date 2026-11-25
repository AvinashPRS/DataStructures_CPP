r"""
AVL tree (self balancing BST) with insert, remove and traversals.
Each node stores its height (number of nodes on the longest path to a leaf).
"""
from collections import deque


class AVL:
    class Node:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None
            self.height = 1

    def __init__(self):
        self.root = None

    # ---------------------------------------------------------- helpers
    def _max_utility(self, current):
        """Maximum value in the subtree."""
        while current.right is not None:
            current = current.right
        return current.data

    @staticmethod
    def _height(current):
        return current.height if current is not None else 0

    def _update_height(self, n):
        n.height = 1 + max(self._height(n.left), self._height(n.right))

    def _right_rotation(self, current):
        """Right rotation if unbalanced on the left."""
        new_node = current.left
        current.left = new_node.right
        new_node.right = current
        self._update_height(current)
        self._update_height(new_node)
        return new_node

    def _left_rotation(self, current):
        """Left rotation if unbalanced on the right."""
        new_node = current.right
        current.right = new_node.left
        new_node.left = current
        self._update_height(current)
        self._update_height(new_node)
        return new_node

    def _in_order_utility(self, current, out):
        if current is None:
            return
        self._in_order_utility(current.left, out)
        out.append(current.data)
        self._in_order_utility(current.right, out)

    def _pre_order_utility(self, current, out):
        if current is None:
            return
        out.append(current.data)
        self._pre_order_utility(current.left, out)
        self._pre_order_utility(current.right, out)

    def _post_order_utility(self, current, out):
        if current is None:
            return
        self._post_order_utility(current.left, out)
        self._post_order_utility(current.right, out)
        out.append(current.data)

    # ---------------------------------------------------------- insert
    def _insert_utility(self, current, value):
        if current is None:
            return self.Node(value)

        if value < current.data:
            current.left = self._insert_utility(current.left, value)
        elif value > current.data:
            current.right = self._insert_utility(current.right, value)

        self._update_height(current)
        balance = self._height(current.left) - self._height(current.right)

        if balance > 1:                       # unbalanced on the left
            if value > current.left.data:     # Left Right case: 5 -> 3 -> 4
                current.left = self._left_rotation(current.left)
            return self._right_rotation(current)  # Left Left case: 5 -> 3 -> 2
        elif balance < -1:                    # unbalanced on the right
            if value < current.right.data:    # Right Left case: 5 -> 7 -> 6
                current.right = self._right_rotation(current.right)
            return self._left_rotation(current)   # Right Right case: 5 -> 6 -> 7
        return current

    # ---------------------------------------------------------- remove
    def _remove_utility(self, current, value):
        if current is None:
            print("Tree is Empty")  # (or value not present)
            return None

        if value < current.data:
            current.left = self._remove_utility(current.left, value)
        elif value > current.data:
            current.right = self._remove_utility(current.right, value)
        else:
            if current.left is None and current.right is None:   # leaf
                return None
            elif current.left is not None and current.right is not None:
                # two children: replace with in-order predecessor
                mx = self._max_utility(current.left)
                current.data = mx
                current.left = self._remove_utility(current.left, mx)
            else:                                                # one child
                current = current.right if current.right is not None else current.left

        self._update_height(current)
        balance = self._height(current.left) - self._height(current.right)

        if balance > 1:
            # Left Left case uses the child's balance
            if self._height(current.left.left) >= self._height(current.left.right):
                return self._right_rotation(current)
            current.left = self._left_rotation(current.left)     # Left Right case
            return self._right_rotation(current)
        elif balance < -1:
            if self._height(current.right.right) >= self._height(current.right.left):
                return self._left_rotation(current)              # Right Right case
            current.right = self._right_rotation(current.right)  # Right Left case
            return self._left_rotation(current)
        return current

    def _display_bfs(self):
        """Display level by level."""
        if self.root is None:
            print("Tree is empty")
            return
        q = deque([self.root])
        out = []
        while q:
            current = q.popleft()
            out.append(current.data)
            if current.left is not None:
                q.append(current.left)
            if current.right is not None:
                q.append(current.right)
        print(" ".join(map(str, out)) + " ")

    # ---------------------------------------------------------- public API
    def insert(self, value):
        self.root = self._insert_utility(self.root, value)

    def remove(self, value):
        self.root = self._remove_utility(self.root, value)

    def _print(self, fn):
        out = []
        fn(self.root, out)
        print(" ".join(map(str, out)) + " ")

    def inorder(self):
        self._print(self._in_order_utility)

    def pre_order(self):
        self._print(self._pre_order_utility)

    def post_order(self):
        self._print(self._post_order_utility)

    def level_order(self):
        self._display_bfs()


def main():
    avl = AVL()
    for v in (9, 5, 10, 0, 6, 11, -1, 1, 2):
        avl.insert(v)
    r"""
    AVL Tree will be
             9
            / \
           1   10
          / \    \
         0   5    11
        /   / \
      -1   2   6
    """
    print("Traversal of the AVL tree is ")
    avl.pre_order()
    avl.level_order()

    avl.remove(10)
    r"""
    After Deletion of 10
             1
            / \
           0   9
          /   / \
        -1   5   11
            / \
           2   6
    """
    print("\nTraversal after deletion of 10")
    avl.pre_order()
    avl.level_order()


if __name__ == "__main__":
    main()
