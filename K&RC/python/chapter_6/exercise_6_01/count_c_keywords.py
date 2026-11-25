"""Exercise 6-1: count C keywords, properly handling underscores, string
constants, comments and preprocessor control lines.

run: python3 count_c_keywords.py < ../../../chapter_6/exercise_6_01/count_c_keywords.c
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


KEYWORDS = [
    "auto", "break", "case", "char", "const", "continue", "default", "do",
    "double", "else", "enum", "extern", "float", "for", "goto", "if", "int",
    "long", "register", "return", "short", "signed", "size_t", "sizeof",
    "static", "struct", "switch", "typedef", "union", "unsigned", "void",
    "volatile", "while",
]


def main():
    counts = [0] * len(KEYWORDS)
    reader = Reader(sys.stdin.read())

    while True:
        word = reader.get_word()
        if word is EOF:
            break
        if word[0].isalpha():
            n = bin_search(word, KEYWORDS)
            if n >= 0:
                counts[n] += 1

    for keyword, count in zip(KEYWORDS, counts):
        if count:
            print("%4d %s" % (count, keyword))


if __name__ == "__main__":
    main()
