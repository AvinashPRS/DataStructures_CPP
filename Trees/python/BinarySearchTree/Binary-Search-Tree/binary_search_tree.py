"""Python port of BinarySearchTree.h - BST with parent pointers."""
import sys

from queue_array import QueueArray
from stack_array import StackArray


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
