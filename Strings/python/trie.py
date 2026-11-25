"""
Trie Implementation for finding the smallest prefix not matching any words
from dictionary.

TC:
    Insert: O(n * L), L: longest string length in dict, n: no. of words in dictionary
    find_shortest_prefix:
        O(min(m, L)), L: longest dict word, m: length of query word
"""


class TrieNode:
    def __init__(self):
        self.is_string = False
        self.leaves = {}


class Trie:
    def __init__(self):
        self._root = TrieNode()

    def insert(self, s):
        """Inserts a string in Trie. Returns False if it was already present."""
        node = self._root
        for c in s:
            # if there is no node with this char, create one,
            # then go further down through the child node
            node = node.leaves.setdefault(c, TrieNode())

        # if the string was already present, we didn't do any insertion
        if node.is_string:
            return False
        node.is_string = True
        return True

    def find_shortest_prefix(self, s):
        """Finds the shortest prefix of s that is not a prefix of any dictionary word"""
        prefix = []
        node = self._root
        # look for the first character for which there is no node in Trie
        for c in s:
            prefix.append(c)
            if c not in node.leaves:
                return "".join(prefix)
            node = node.leaves[c]
        return ""


if __name__ == "__main__":
    trie = Trie()
    word = "army"
    dictionary = {"arm", "cat", "piano", "germ"}

    for w in dictionary:
        trie.insert(w)

    print(trie.find_shortest_prefix(word))
