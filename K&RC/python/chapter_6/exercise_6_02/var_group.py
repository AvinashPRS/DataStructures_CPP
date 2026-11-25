"""Exercise 6-2: read a C program and print in alphabetical order each group
of variable names that are identical in the first N characters (default 6).

run: python3 var_group.py 5 < test.txt
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


DATA_TYPES = ["char", "double", "float", "int", "long", "short", "void"]

var_name_str_cmp_len = 6


class TreeNode:
    def __init__(self, word):
        self.word = word
        self.left = None
        self.right = None


class ListNode:
    def __init__(self, word):
        self.var_group = add_to_tree(None, word)
        self.next = None


def add_to_tree(node, word):
    if node is None:
        return TreeNode(word)
    if word < node.word:
        node.left = add_to_tree(node.left, word)
    elif word > node.word:
        node.right = add_to_tree(node.right, word)
    return node


def print_tree(node):
    if node is not None:
        print_tree(node.left)
        print(node.word)
        print_tree(node.right)


def add_to_list(node, word):
    if node is None:
        return ListNode(word)
    n = var_name_str_cmp_len
    if node.var_group.word[:n] == word[:n]:
        node.var_group = add_to_tree(node.var_group, word)
    else:
        node.next = add_to_list(node.next, word)
    return node


def print_list(node):
    while node is not None:
        print_tree(node.var_group)
        print()
        node = node.next


def parse_arg_list(args):
    global var_name_str_cmp_len
    if len(args) > 1:
        return False
    if len(args) == 1:
        if not args[0].isdigit():
            return False
        var_name_str_cmp_len = int(args[0])
    return True


def main(argv):
    if not parse_arg_list(argv[1:]):
        print("Error: invalid arguments.")
        return 1

    list_root = None
    reader = Reader(sys.stdin.read())

    while True:
        word = reader.get_word()
        if word is EOF:
            break
        if bin_search(word, DATA_TYPES) >= 0:
            while True:
                # NOTE: both variable and function names are considered.
                word = reader.get_word()
                if word is not EOF and (word[0].isalpha() or word[0] == "_"):
                    list_root = add_to_list(list_root, word)
                if reader.get_word() != ",":
                    break

    print_list(list_root)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
