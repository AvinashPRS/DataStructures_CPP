"""
Python port of the GeeksForGeeks AVL tree.

Operation      Description                                     Time      Space
Insert         Inserts a new element into the tree             O(log n)  O(log n)
Delete Node    Removes an element from the tree                O(log n)  O(log n)
Search         Searches for an element in the tree             O(log n)  O(1)
Rotate Left    Performs left rotation to balance the AVL tree  O(1)      O(1)
Rotate Right   Performs right rotation to balance the AVL tree O(1)      O(1)
"""


class AVLNode:
    """A node in the AVL tree."""

    def __init__(self, k):
        self.key = k
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None

    # ------------------------------------------------------------ helpers
    @staticmethod
    def _height(node):
        return node.height if node is not None else 0

    def _balance_factor(self, node):
        """Balance factor is height(left) - height(right)."""
        if node is None:
            return 0
        return self._height(node.left) - self._height(node.right)

    def _update_height(self, node):
        node.height = 1 + max(self._height(node.left), self._height(node.right))

    def _right_rotate(self, y):
        x = y.left
        t2 = x.right
        x.right = y
        y.left = t2
        self._update_height(y)
        self._update_height(x)
        return x

    def _left_rotate(self, x):
        y = x.right
        t2 = y.left
        y.left = x
        x.right = t2
        self._update_height(x)
        self._update_height(y)
        return y

    def _rebalance(self, node):
        balance = self._balance_factor(node)
        if balance > 1:                                   # left heavy
            if self._balance_factor(node.left) < 0:       # LR
                node.left = self._left_rotate(node.left)
            return self._right_rotate(node)               # LL
        if balance < -1:                                  # right heavy
            if self._balance_factor(node.right) > 0:      # RL
                node.right = self._right_rotate(node.right)
            return self._left_rotate(node)                # RR
        return node

    # ------------------------------------------------------------ insert
    def _insert(self, node, key):
        # normal BST insertion
        if node is None:
            return AVLNode(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        else:
            return node
        self._update_height(node)
        return self._rebalance(node)

    @staticmethod
    def _min_value_node(node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    # ------------------------------------------------------------ delete
    def _delete_node(self, root, key):
        """
        Search for the node to delete.
        - leaf: remove it
        - one child: replace it with its child
        - two children: copy the in-order successor (min of right subtree)
          into the node and delete the successor from the right subtree
        Then update the height, compute the balance factor and rotate:
          Left-Left: right rotation
          Left-Right: left rotation on left child, then right rotation
          Right-Right: left rotation
          Right-Left: right rotation on right child, then left rotation
        """
        if root is None:
            return root
        if key < root.key:
            root.left = self._delete_node(root.left, key)
        elif key > root.key:
            root.right = self._delete_node(root.right, key)
        else:
            if root.left is None or root.right is None:
                temp = root.left if root.left else root.right
                if temp is None:
                    return None
                root = temp
            else:
                temp = self._min_value_node(root.right)
                root.key = temp.key
                root.right = self._delete_node(root.right, temp.key)

        self._update_height(root)
        return self._rebalance(root)

    def _inorder(self, root, out):
        if root is not None:
            self._inorder(root.left, out)
            out.append(root.key)
            self._inorder(root.right, out)

    def _search(self, root, key):
        while root is not None:
            if root.key == key:
                return True
            root = root.left if key < root.key else root.right
        return False

    # ------------------------------------------------------------ public
    def insert(self, key):
        self.root = self._insert(self.root, key)

    def remove(self, key):
        self.root = self._delete_node(self.root, key)

    def search(self, key):
        return self._search(self.root, key)

    def print_inorder(self):
        out = []
        self._inorder(self.root, out)
        print(" ".join(map(str, out)) + " ")


def main():
    avl = AVLTree()
    for v in (10, 20, 30, 40, 50, 25):
        avl.insert(v)

    print("Inorder traversal of the AVL tree: ", end="")
    avl.print_inorder()

    avl.remove(30)
    print("Inorder traversal after removing 30: ", end="")
    avl.print_inorder()

    print("Is 25 in the tree?", "Yes" if avl.search(25) else "No")
    print("Is 30 in the tree?", "Yes" if avl.search(30) else "No")


if __name__ == "__main__":
    main()
