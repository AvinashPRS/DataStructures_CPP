"""Exercise 5-19: undcl that doesn't add redundant parentheses.

Converts word descriptions into C declarations, e.g.
    x () * [] * () char  ->  char (*(*x())[])()

run: python3 undcl.py < test.txt
"""
import sys

EOF = None
NAME, PARENS, BRACKETS = "NAME", "PARENS", "BRACKETS"
PAREN_OPEN, PAREN_CLOSE = "(", ")"
BRACKET_OPEN, BRACKET_CLOSE = "[", "]"


class Lexer:
    """Character reader over stdin with unlimited pushback (like ungetc)."""

    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.pushed = []
        self.token = ""
        self.next_token = None

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

    def get_name(self):
        chars = []
        c = self.getc()
        while c is not EOF and (c.isalnum() or c == "_"):
            chars.append(c)
            c = self.getc()
        self.ungetc(c)
        return "".join(chars)

    def get_next_token(self):
        self.skip_blanks()
        self.skip_comments()
        self.skip_blanks()

        c = self.getc()
        if c == "(":
            self.skip_blanks()
            c = self.getc()
            if c == ")":
                self.token = "()"
                self.next_token = PARENS
                return PARENS
            self.ungetc(c)
            self.next_token = PAREN_OPEN
            return PAREN_OPEN
        if c == "[":
            self.skip_blanks()
            self.token = self.get_name()
            self.skip_blanks()
            c = self.getc()
            if c == "]":
                self.next_token = BRACKETS
                return BRACKETS
            self.ungetc(c)
            self.next_token = BRACKET_OPEN
            return BRACKET_OPEN
        if c is not EOF and c.isalpha():
            self.ungetc(c)
            self.token = self.get_name()
            self.next_token = NAME
            return NAME

        self.next_token = c
        return c


def main():
    lx = Lexer(sys.stdin.read())

    while lx.get_next_token() is not EOF:
        out = lx.token

        while lx.get_next_token() not in ("\n", EOF):
            if lx.next_token == PARENS:
                if out.startswith("*"):
                    out = "(%s)" % out
                out += lx.token
            elif lx.next_token == BRACKETS:
                if out.startswith("*"):
                    out = "(%s)" % out
                out += "[%s]" % lx.token
            elif lx.next_token == "*":
                out = "*" + out
            elif lx.next_token == NAME:
                out = "%s %s" % (lx.token, out)
            else:
                print("Syntax Error: Invalid input at %s." % lx.token)

        print(out)


if __name__ == "__main__":
    main()
