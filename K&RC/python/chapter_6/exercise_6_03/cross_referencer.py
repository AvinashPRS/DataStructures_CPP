"""Exercise 6-3: cross-referencer that prints a list of all words in a
document and, for each word, the line numbers on which it occurs.
Noise words like "the", "and" are removed.

run: python3 cross_referencer.py < test.txt
"""
import sys

EOF = None


class Reader:
    """Character reader over a string with unlimited pushback (ungetc)."""

    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.pushed = []

    def getc(self):
        if self.pushed:
            return self.pushed.pop()
        if self.pos < len(self.text):
            c = self.text[self.pos]
            self.pos += 1
            return c
        return EOF

    def ungetc(self, c):
        if c is not EOF:
            self.pushed.append(c)

    def skip_blanks(self):
        c = self.getc()
        while c in (" ", "\t"):
            c = self.getc()
        self.ungetc(c)

    def skip_comments(self):
        c = self.getc()
        if c == "/":
            c = self.getc()
            if c == "/":
                c = self.getc()
                while c != "\n" and c is not EOF:
                    c = self.getc()
            elif c == "*":
                c = self.getc()
                while c != "*" and c is not EOF:
                    c = self.getc()
                c = self.getc()
                if c == "/":
                    self.ungetc("\n")
                    return
        self.ungetc(c)

    def skip_chars_between(self, start, end):
        c = self.getc()
        if c == start:
            c = self.getc()
            while c is not EOF:
                if c == "\\":
                    c = self.getc()
                    if c is EOF:
                        break
                elif c == end:
                    return
                c = self.getc()
        self.ungetc(c)

    def skip_char_literal(self):
        self.skip_chars_between("'", "'")

    def skip_string_literal(self):
        self.skip_chars_between("\"", "\"")

    def get_word(self, skip_code=True):
        """Return the next word, a single non-word character, or EOF."""
        self.skip_blanks()
        if skip_code:
            self.skip_comments()
            self.skip_char_literal()
            self.skip_string_literal()

        c = self.getc()
        if c is EOF:
            return EOF
        if not c.isalpha() and c != "_":
            return c

        word = [c]
        c = self.getc()
        while c is not EOF and (c.isalnum() or c == "_"):
            word.append(c)
            c = self.getc()
        self.ungetc(c)
        return "".join(word)


def bin_search(word, arr):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if word < arr[mid]:
            high = mid - 1
        elif word > arr[mid]:
            low = mid + 1
        else:
            return mid
    return -1


LINKING_WORDS = [
    "And", "As", "But", "For", "Like", "Nor", "Or", "So", "The",
    "Then", "To", "Too", "Yet", "and", "as", "but", "for", "like",
    "nor", "or", "so", "the", "then", "to", "too", "yet",
]


class TreeNode:
    def __init__(self, word, line_number):
        self.word = word
        self.line_numbers = [line_number]
        self.left = None
        self.right = None


def add_to_tree(node, word, line_number):
    if node is None:
        return TreeNode(word, line_number)
    if word == node.word:
        node.line_numbers.append(line_number)
    elif word < node.word:
        node.left = add_to_tree(node.left, word, line_number)
    else:
        node.right = add_to_tree(node.right, word, line_number)
    return node


def print_tree(node):
    if node is not None:
        print_tree(node.left)
        print("%s: %s" % (node.word, ", ".join(str(n) for n in node.line_numbers)))
        print_tree(node.right)


def main():
    line_number = 1
    tree_root = None
    reader = Reader(sys.stdin.read())

    while True:
        word = reader.get_word(skip_code=False)
        if word is EOF:
            break
        if word == "\n":
            line_number += 1
        elif word[0].isalpha():
            if bin_search(word, LINKING_WORDS) == -1:
                tree_root = add_to_tree(tree_root, word, line_number)

    print_tree(tree_root)


if __name__ == "__main__":
    main()
