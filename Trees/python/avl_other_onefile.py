"""
AVL tree with order statistics (originally by Kadir Emre Oto, 06.08.2018).

Each node stores `count` (number of nodes in its subtree) so the tree also
supports indexing (tree[i] is the i-th smallest value), find (rank of a value),
lower_bound and upper_bound.

The C++ version walks the tree with pointers-to-pointers (node **) so the same
code can replace the root or any child link. Here a small `_Slot` object plays
that role: it refers to "attribute `name` of object `owner`".
"""
import random


class AVLTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.count = 1    # how many nodes are in this subtree
        self.height = 1

    def update_values(self):
        self.count = ((self.left.count if self.left else 0) +
                      (self.right.count if self.right else 0) + 1)
        self.height = max(self.left.height if self.left else 0,
                          self.right.height if self.right else 0) + 1

    def balance_factor(self):
        """height(left) - height(right)"""
        return ((self.left.height if self.left else 0) -
                (self.right.height if self.right else 0))

    def left_rotate(self):
        r = self.right
        self.right = r.left
        r.left = self
        self.update_values()  # the order is important
        r.update_values()
        return r

    def right_rotate(self):
        l = self.left
        self.left = l.right
        l.right = self
        self.update_values()  # the order is important
        l.update_values()
        return l


class _Slot:
    """A reference to a child link (or the root link): owner.<name>."""
    __slots__ = ("owner", "name")

    def __init__(self, owner, name):
        self.owner = owner
        self.name = name

    def get(self):
        return getattr(self.owner, self.name)

    def set(self, node):
        setattr(self.owner, self.name, node)


class AVLTree:
    def __init__(self):
        self.root = None
        self._size = 0

    def clear(self):
        self.root = None
        self._size = 0

    def insert(self, value):
        indirect = _Slot(self, "root")
        path = []  # to update height values
        while indirect.get() is not None:
            path.append(indirect)
            node = indirect.get()
            indirect = _Slot(node, "left" if node.value > value else "right")
        indirect.set(AVLTreeNode(value))
        path.append(indirect)
        self._balance(path)
        self._size += 1

    def erase(self, value):
        indirect = _Slot(self, "root")
        path = []
        while indirect.get() is not None and indirect.get().value != value:
            path.append(indirect)
            node = indirect.get()
            indirect = _Slot(node, "left" if node.value > value else "right")

        if indirect.get() is None:  # the value does not exist in tree
            return
        path.append(indirect)

        index = len(path)
        node = indirect.get()
        if node.left is None and node.right is None:       # leaf
            indirect.set(None)
            path.pop()
        elif node.right is None:                           # only left child
            indirect.set(node.left)
            path.pop()
        else:                                              # right child exists
            successor = _Slot(node, "right")
            while successor.get().left is not None:
                path.append(successor)
                successor = _Slot(successor.get(), "left")
            suc = successor.get()
            if suc is node.right:
                suc.left = node.left
                indirect.set(suc)
            else:
                tmp = path[-1].get()
                tmp.left = suc.right
                suc.left = node.left
                suc.right = node.right
                indirect.set(suc)
                # the first successor-chain entry pointed at node.right,
                # which now hangs off suc.right
                path[index] = _Slot(suc, "right")
        self._balance(path)
        self._size -= 1

    def _balance(self, path):
        """Update and rebalance bottom-up along the path."""
        for indirect in reversed(path):
            node = indirect.get()
            node.update_values()
            bf = node.balance_factor()
            if bf >= 2 and node.left.balance_factor() >= 0:      # left - left
                indirect.set(node.right_rotate())
            elif bf >= 2:                                        # left - right
                node.left = node.left.left_rotate()
                indirect.set(node.right_rotate())
            elif bf <= -2 and node.right.balance_factor() <= 0:  # right - right
                indirect.set(node.left_rotate())
            elif bf <= -2:                                       # right - left
                node.right = node.right.right_rotate()
                indirect.set(node.left_rotate())

    def empty(self):
        return self._size == 0

    def size(self):
        return self._size

    __len__ = size

    def find(self, value):
        """Index (rank) of value, or -1."""
        direct = self.root
        idx = 0
        while direct is not None and direct.value != value:
            if direct.value > value:
                direct = direct.left
            else:
                idx += (direct.left.count if direct.left else 0) + 1
                direct = direct.right
        if direct is None:
            return -1
        return idx + (direct.left.count if direct.left else 0)

    def upper_bound(self, value):
        """Number of elements <= value."""
        direct, idx = self.root, 0
        while direct is not None:
            if direct.value > value:
                direct = direct.left
            else:
                idx += (direct.left.count if direct.left else 0) + 1
                direct = direct.right
        return idx

    def lower_bound(self, value):
        """Number of elements < value."""
        direct, idx = self.root, 0
        while direct is not None:
            if direct.value >= value:
                direct = direct.left
            else:
                idx += (direct.left.count if direct.left else 0) + 1
                direct = direct.right
        return idx

    def __getitem__(self, idx):
        """idx-th smallest value."""
        if not 0 <= idx < self._size:
            raise IndexError(idx)
        cur = self.root
        left = cur.left.count if cur.left else 0
        while left != idx:
            if left < idx:
                idx -= left + 1
                cur = cur.right
            else:
                cur = cur.left
            left = cur.left.count if cur.left else 0
        return cur.value

    def display(self):
        print()
        if self.root is not None:
            self._display(self.root)
        else:
            print("Empty", end="")
        print()

    def _display(self, cur, depth=0, state=0):
        """state: 1 -> left, 2 -> right, 0 -> root"""
        if cur.left:
            self._display(cur.left, depth + 1, 1)
        prefix = "     " * depth + ("┌───" if state == 1 else "└───" if state == 2 else "")
        print("%s[%s] - (%d, %d)" % (prefix, cur.value, cur.count, cur.height))
        if cur.right:
            self._display(cur.right, depth + 1, 2)


def main():
    tree = AVLTree()
    size = 10
    for _ in range(size):
        tree.insert(random.randint(0, 2 ** 31 - 1))
    for i in range(tree.size()):
        print(tree[i])
    tree.clear()
    print(tree.size())


if __name__ == "__main__":
    main()
