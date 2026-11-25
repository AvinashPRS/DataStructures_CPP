"""Exercise 5-18: make dcl recover from input errors.

Converts C declarations into word descriptions, e.g.
    char **argv  ->  argv: pointer to pointer to char

run: python3 dcl.py < test.txt
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


class Dcl:
    def __init__(self, lexer):
        self.lx = lexer
        self.name = ""
        self.out = ""

    def dcl(self):
        nr_of_stars = 0
        while self.lx.get_next_token() == "*":
            nr_of_stars += 1

        self.dir_dcl()

        self.out += " pointer to" * nr_of_stars

    def dir_dcl(self):
        lx = self.lx
        if lx.next_token == PAREN_OPEN:
            self.dcl()
            if lx.next_token != PAREN_CLOSE:
                print("Syntax Error: missing ')'.")
        elif lx.next_token == NAME:
            self.name = lx.token
        else:
            print("Syntax Error: expected name or (dcl).")

        while lx.get_next_token() in (PARENS, BRACKETS):
            if lx.next_token == PARENS:
                self.out += " function returning"
            else:
                self.out += " array[" + lx.token + "] of"


def main():
    lx = Lexer(sys.stdin.read())
    parser = Dcl(lx)

    while lx.get_next_token() is not EOF:
        if lx.next_token == "\n":
            continue

        data_type = lx.token
        parser.out = ""
        parser.name = ""

        parser.dcl()

        if lx.next_token != "\n":
            if lx.next_token == NAME:
                print("Syntax Error: '%s' unexpected." % lx.token)
            else:
                print("Syntax Error: '%s' unexpected." % (lx.next_token or "EOF"))

            while lx.next_token not in ("\n", EOF):
                lx.get_next_token()
        else:
            print("%s:%s %s" % (parser.name, parser.out, data_type))


if __name__ == "__main__":
    main()
