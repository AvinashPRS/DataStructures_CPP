"""Exercise 6-6: a simple version of the #define processor (no arguments)
suitable for C programs, based on the hash table routines (lookup, install,
undef).

run: python3 define.py < ../../../chapter_6/exercise_6_06/define.c
"""
import sys

HASH_SIZE = 101
SIZE_T_MASK = (1 << 64) - 1
EOF = None


class ListNode:
    def __init__(self, name, definition, next_node):
        self.name = name
        self.definition = definition
        self.next = next_node


hash_table = [None] * HASH_SIZE


def hash_(s):
    h = 0
    for ch in s:
        h = (ord(ch) + 31 * h) & SIZE_T_MASK
    return h % HASH_SIZE


def lookup(s):
    node = hash_table[hash_(s)]
    while node is not None:
        if node.name == s:
            return node
        node = node.next
    return None


def install(name, definition):
    node = lookup(name)
    if node is None:
        h = hash_(name)
        node = ListNode(name, definition, hash_table[h])
        hash_table[h] = node
    else:
        node.definition = definition
    return node


def undef(name):
    h = hash_(name)
    prev, node = None, hash_table[h]
    while node is not None:
        if node.name == name:
            if prev is None:
                hash_table[h] = node.next
            else:
                prev.next = node.next
            return True
        prev, node = node, node.next
    return False


class Processor:
    def __init__(self, text, out):
        self.text = text
        self.pos = 0
        self.pushed = []
        self.out = out

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

    def put(self, c):
        if c is not EOF:
            self.out.write(c)

    def get_word(self):
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

    def get_alnum_str(self):
        chars = []
        c = self.getc()
        while c is not EOF and c.isalnum():
            chars.append(c)
            c = self.getc()
        self.ungetc(c)
        return "".join(chars)

    def consume_word(self, error_str):
        word = self.get_word()
        if word is EOF:
            return ""
        if not word[0].isalpha():
            print(error_str)
        self.out.write(word)
        return word

    def consume_blanks(self):
        c = self.getc()
        while c in (" ", "\t"):
            self.put(c)
            c = self.getc()
        self.ungetc(c)

    def consume_comments(self):
        c = self.getc()
        if c == "/":
            self.put(c)
            c = self.getc()
            if c == "/":
                self.put(c)
                c = self.getc()
                while c != "\n" and c is not EOF:
                    self.put(c)
                    c = self.getc()
            elif c == "*":
                self.put(c)
                prev = ""
                c = self.getc()
                while c is not EOF:
                    self.put(c)
                    if prev == "*" and c == "/":
                        return
                    prev = c
                    c = self.getc()
        self.ungetc(c)

    def consume_chars_between(self, start, end):
        c = self.getc()
        if c == start:
            self.put(c)
            c = self.getc()
            while c is not EOF:
                self.put(c)
                if c == "\\":
                    c = self.getc()
                    self.put(c)
                    if c is EOF:
                        break
                elif c == end:
                    return
                c = self.getc()
        self.ungetc(c)

    def consume_preproc(self):
        c = self.getc()
        if c != "#":
            self.ungetc(c)
            return
        self.put(c)

        word = self.consume_word("Error: expected preprocessor directive.")
        directive = word if word in ("define", "undef") else None

        if directive:
            self.consume_blanks()
            word = self.consume_word("Error: invalid name.")

        if directive == "define":
            self.consume_blanks()
            definition = self.get_alnum_str()
            self.out.write(definition)

            node = lookup(definition)
            install(word, node.definition if node is not None else definition)
        elif directive == "undef":
            undef(word)

    def run(self):
        while True:
            word = self.get_word()
            if word is EOF:
                break
            c = word[0]
            if c.isalpha():
                node = lookup(word)
                self.out.write(node.definition if node is not None else word)
            elif c == "/":
                self.ungetc(c)
                self.consume_comments()
            elif c == "'":
                self.ungetc(c)
                self.consume_chars_between("'", "'")
            elif c == '"':
                self.ungetc(c)
                self.consume_chars_between('"', '"')
            elif c == "#":
                self.ungetc(c)
                self.consume_preproc()
            else:
                self.out.write(word)


def main():
    Processor(sys.stdin.read(), sys.stdout).run()


if __name__ == "__main__":
    main()
