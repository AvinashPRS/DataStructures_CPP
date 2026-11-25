"""
Single file Binary Search Tree with an array based Stack and Queue
(Python port of BinarySearchTree.cpp).
"""
import random
import sys
from abc import ABC, abstractmethod


# ---------- STACK ----------
class Stack(ABC):
    @abstractmethod
    def push(self, e): ...

    @abstractmethod
    def pop(self): ...

    @abstractmethod
    def is_empty(self): ...


class StackOverflow(Exception):
    def __str__(self):
        return "Stack overflow"


class StackUnderflow(Exception):
    def __str__(self):
        return "Stack underflow"


class WrongStackSize(Exception):
    def __str__(self):
        return "Wrong stack size_"


class StackArray(Stack):
    def __init__(self, s):
        if s <= 0:
            raise WrongStackSize()
        self.size_ = s
        self.top_ = -1
        self.arr_ = [None] * s

    def push(self, element):
        if self.top_ == self.size_ - 1:
            raise StackOverflow()
        self.top_ += 1
        self.arr_[self.top_] = element

    def pop(self):
        if self.top_ == -1:
            raise StackUnderflow()
        element = self.arr_[self.top_]
        self.top_ -= 1
        return element

    def is_empty(self):
        return self.top_ == -1

    def top(self):
        if self.is_empty():
            raise StackUnderflow()
        return self.arr_[self.top_]


# ---------- QUEUE ----------
class Queue(ABC):
    @abstractmethod
    def en_queue(self, e): ...   # adding an item to the queue

    @abstractmethod
    def de_queue(self): ...      # removing the front element

    @abstractmethod
    def is_empty(self): ...      # checking the queue for emptiness


class QueueOverflow(Exception):
    def __str__(self):
        return "Queue is full!"


class QueueUnderflow(Exception):
    def __str__(self):
        return "Queue is empty!"


class WrongQueueSize(Exception):
    def __str__(self):
        return "Wrong queue size_!"


class QueueArray(Queue):
    def __init__(self, size_):
        if size_ <= 0:
            raise WrongQueueSize()
        self.size_ = size_
        self.head_ = -1
        self.tail_ = -1
        self.queue_array_ = [None] * size_

    def en_queue(self, element):
        if self.head_ == -1:
            self.head_ = 0
        if self.tail_ == self.size_ - 1:
            raise QueueOverflow()
        self.tail_ += 1
        self.queue_array_[self.tail_] = element

    def de_queue(self):
        if self.is_empty():
            raise QueueUnderflow()
        item = self.queue_array_[self.head_]
        self.head_ += 1
        if self.head_ > self.tail_:
            self.head_ = self.tail_ = -1
        return item

    def is_empty(self):
        return self.head_ == -1 and self.tail_ == -1


# ---------- BINARY SEARCH TREE ----------
class BinarySearchTree:
    class Node:
        def __init__(self, key, left=None, right=None, p=None):
            self.key_ = key      # the key value contained in the node
            self.left_ = left    # left subtree
            self.right_ = right  # right subtree
            self.p_ = p          # parent

    def __init__(self):
        self.root_ = None

    # 1.2 Searching the node by key
    def _iterative_search_node(self, key):
        current = self.root_
        while current is not None and key != current.key_:
            current = current.left_ if key < current.key_ else current.right_
        return current

    # 4.2 Recursive function to output a tree image: key(left)(right)
    def _print_node(self, out, root):
        if root:
            out.write(str(root.key_))
            if root.left_ or root.right_:
                out.write("(")
                if root.left_:
                    self._print_node(out, root.left_)
                out.write(")(")
                if root.right_:
                    self._print_node(out, root.right_)
                out.write(")")

    # 5.2 Number of nodes
    def _get_count(self, node):
        if node is None:
            return 0
        return 1 + self._get_count(node.left_) + self._get_count(node.right_)

    # 6.2 Height (empty tree = -1, single node = 0)
    def _get_height(self, node):
        if node is None:
            return -1
        return 1 + max(self._get_height(node.left_), self._get_height(node.right_))

    # 8.2 Recursive inorder traversal
    def _inorder_walk(self, node):
        if node:
            self._inorder_walk(node.left_)
            print(node.key_, end=" ")
            self._inorder_walk(node.right_)

    def _is_similar_helper(self, root1, root2):
        """Same shape (keys are ignored)."""
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        return (self._is_similar_helper(root1.left_, root2.left_) and
                self._is_similar_helper(root1.right_, root2.right_))

    def _keys(self, node, out):
        if node:
            self._keys(node.left_, out)
            out.append(node.key_)
            self._keys(node.right_, out)
        return out

    # 1.1 Key search
    def iterative_search(self, key):
        return self._iterative_search_node(key) is not None

    # 2 Insert: True if added, False if the key was already there
    def insert(self, key):
        parent, current = None, self.root_
        while current is not None:
            parent = current
            if key == current.key_:
                return False
            current = current.left_ if key < current.key_ else current.right_
        new_node = self.Node(key, p=parent)
        if parent is None:
            self.root_ = new_node
        elif key < parent.key_:
            parent.left_ = new_node
        else:
            parent.right_ = new_node
        return True

    def _transplant(self, u, v):
        """Replace subtree rooted at u with subtree rooted at v."""
        if u.p_ is None:
            self.root_ = v
        elif u is u.p_.left_:
            u.p_.left_ = v
        else:
            u.p_.right_ = v
        if v is not None:
            v.p_ = u.p_

    # 3.1 Delete: True if deleted, False if the key was not there
    def delete_key(self, key):
        node = self._iterative_search_node(key)
        if node is None:
            return False
        if node.left_ is None:                 # leaf or only right child
            self._transplant(node, node.right_)
        elif node.right_ is None:              # only left child
            self._transplant(node, node.left_)
        else:                                  # two children
            # successor = min of right subtree; it has no left child
            succ = node.right_
            while succ.left_ is not None:
                succ = succ.left_
            node.key_ = succ.key_
            self._transplant(succ, succ.right_)
        return True

    # 4.1 Print a string image of the tree
    def print(self, out=sys.stdout):
        if self.root_:
            self._print_node(out, self.root_)
        out.write("\n")

    # 5.1
    def get_count(self):
        return self._get_count(self.root_)

    # 6.1
    def get_height(self):
        return self._get_height(self.root_)

    # 7 Infix traversal (iterative, with StackArray)
    def iterative_inorder_walk(self):
        if self.root_ is None:
            return
        stack = StackArray(self.get_count())
        current = self.root_
        while current is not None or not stack.is_empty():
            if current is not None:
                stack.push(current)
                current = current.left_
            else:
                current = stack.pop()
                print(current.key_, end=" ")
                current = current.right_

    # 8.1 Infix traversal (recursive)
    def inorder_walk(self):
        self._inorder_walk(self.root_)

    # 9 Level order (breadth first, with QueueArray)
    def walk_by_levels(self):
        if self.root_ is None:
            return
        queue = QueueArray(self.get_count())
        queue.en_queue(self.root_)
        while not queue.is_empty():
            current = queue.de_queue()
            print(current.key_, end=" ")
            if current.left_:
                queue.en_queue(current.left_)
            if current.right_:
                queue.en_queue(current.right_)

    # 10 Are two trees similar (same structure)
    def is_similar(self, other):
        return self._is_similar_helper(self.root_, other.root_)

    # 11 Is there any key present in both search trees
    def is_identical_key(self, other):
        mine = self._keys(self.root_, [])
        return any(other.iterative_search(k) for k in mine)


def main():
    print("test 1")
    test = BinarySearchTree()
    for _ in range(10):
        test.insert(random.randrange(20))
    test.print(sys.stdout)

    print("Count:", test.get_count())
    print("Height:", test.get_height())

    print("iterative inorder walk: ", end="")
    test.iterative_inorder_walk()
    print("\ninorder walk: ", end="")
    test.inorder_walk()
    print("\nwalk by levels: ", end="")
    test.walk_by_levels()

    print("\n\nTest 2")
    test1 = BinarySearchTree()
    for v in (4, 2, 6, 1):
        test1.insert(v)
    test1.print(sys.stdout)

    print("Is 4 in tree:", int(test1.iterative_search(4)))
    print("Is 9 in tree:", int(test1.iterative_search(9)))
    print("Let's add 6", int(test1.insert(6)))
    print("Let's delete 6", int(test1.delete_key(6)))
    print("Let's delete 6", int(test1.delete_key(6)))
    print("Is 6 in tree:", int(test1.iterative_search(6)))
    print()
    test1.insert(6)

    print("Test 3")
    test2 = BinarySearchTree()
    for v in (4, 2, 6, 1):
        test2.insert(v)
    test2.print(sys.stdout)

    print("are similar tree 2 and tree 3:", int(test2.is_similar(test1)))
    print("are identical keys in tree 2 and tree 3:", int(test2.is_identical_key(test1)))
    print("Let's add 15 in tree 3", int(test2.insert(15)))
    print("are similar tree 2 and tree 3:", int(test2.is_similar(test1)))
    print("are identical keys in tree 2 and tree 3:", int(test2.is_identical_key(test1)))


if __name__ == "__main__":
    main()
