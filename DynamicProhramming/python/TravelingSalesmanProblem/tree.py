"""
tree.py - A binary search tree of cities, sorted by relative distance to an
owner city. Python port of the C++ version written by Sam Best for CS202/CS325.

The following operators are overloaded:
 +=: adds a tree or a city to an existing tree
 + : used with any combination of trees and cities. Final value is a tree.
 str(): list of each city id in sorted order
 ==: compares two trees, True if the contents are the same (in position and value)
 !=: compares two trees, True if the contents differ (in position or value)
"""
from city import City


class TreeNode:
    def __init__(self):
        self.tree_city = None
        self.left = None
        self.right = None

    def set_city(self, city_in):
        if city_in is None:
            return 0
        self.tree_city = city_in
        return 1

    def get_city(self):
        return self.tree_city


class Tree:
    def __init__(self, city_in=None):
        self.owner_city = city_in
        self.root = None

    def __copy__(self):
        new_tree = Tree(self.owner_city)
        new_tree.root = self._copy(self.root)
        return new_tree

    @staticmethod
    def _copy(source):
        """Recursive copy"""
        if source is None:
            return None
        dest = TreeNode()
        dest.set_city(source.get_city())
        dest.left = Tree._copy(source.left)
        dest.right = Tree._copy(source.right)
        return dest

    def add_to_tree(self, to_add):
        """Adds a new city to the tree"""
        self.root = self._insert(self.root, to_add)

    def _insert(self, root, to_add):
        """Recursive insert"""
        if root is None:
            root = TreeNode()
            root.set_city(to_add)
        elif root.get_city().dist(self.owner_city) < self.owner_city.dist(to_add):
            root.left = self._insert(root.left, to_add)
        else:
            root.right = self._insert(root.right, to_add)
        return root

    def display_detailed_tree(self):
        self._traverse_and_display(self.root)

    def _traverse_and_display(self, root):
        if root is None:
            return
        self._traverse_and_display(root.right)
        print(root.get_city().dist(self.owner_city))
        self._traverse_and_display(root.left)

    def _traverse_and_add(self, source, dest):
        """Post-order traversal, adding each city from the source tree to dest"""
        if source is None:
            return
        self._traverse_and_add(source.left, dest)
        self._traverse_and_add(source.right, dest)
        dest.add_to_tree(source.get_city())

    def clear_tree(self):
        """Removes all nodes from the tree"""
        self.root = None

    def _is_equal(self, root_one, root_two):
        """Recursively compares each node of two trees -- if any differ, returns False"""
        if (root_one is None) != (root_two is None):
            return False
        if root_one is None and root_two is None:
            return True
        # NOTE: the original C++ negates compare() here, which looks like a bug;
        # kept as-is to preserve behaviour.
        return (not root_one.get_city().compare(root_two.get_city())
                and self._is_equal(root_one.left, root_two.left)
                and self._is_equal(root_one.right, root_two.right))

    def build_neighbor_list(self, neighbor_list, size):
        self._traverse_and_build(self.root, neighbor_list, size)

    def _traverse_and_build(self, root, neighbor_list, size):
        if root is None:
            return
        self._traverse_and_build(root.right, neighbor_list, size - 1)
        neighbor_list.append(root.get_city())
        self._traverse_and_build(root.left, neighbor_list, size - 1)

    # ***************************OPERATORS***************************
    def __iadd__(self, to_add):
        if isinstance(to_add, City):
            self.add_to_tree(to_add)
        else:
            # if the same object is passed, copy it first
            source = to_add.__copy__() if to_add is self else to_add
            self._traverse_and_add(source.root, self)
        return self

    def __add__(self, other):
        if isinstance(other, City):
            temp = self.__copy__()
            temp.add_to_tree(other)
            return temp
        temp = other.__copy__()
        self._traverse_and_add(self.root, temp)
        return temp

    def __radd__(self, city_in):
        temp = self.__copy__()
        temp.add_to_tree(city_in)
        return temp

    def __eq__(self, tree_in):
        if self is tree_in:
            return True
        if self.root is None and tree_in.root is None:
            return True
        return self._is_equal(self.root, tree_in.root)

    def __ne__(self, tree_in):
        return not self.__eq__(tree_in)

    def __str__(self):
        """Ordered list of the city ids in the tree"""
        lines = []
        traverse_and_output(lines, self.root)
        return "".join(line + "\n" for line in lines)


def traverse_and_output(output, root):
    """Recursively outputs all city ids in a BST"""
    if root is None:
        return
    traverse_and_output(output, root.left)
    output.append(str(root.get_city().get_id()))
    traverse_and_output(output, root.right)
