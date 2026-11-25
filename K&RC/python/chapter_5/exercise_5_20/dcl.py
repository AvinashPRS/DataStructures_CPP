"""Exercise 5-20: expand dcl to handle declarations with function argument
types, qualifiers like const, and so on.

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


ATTR_SEPARATOR = ","

DATA_TYPES = ("void", "char", "short", "int", "long", "float", "double",
              "custom_type")


def is_valid_qualifier(s):
    return s in ("const", "volatile")


def is_valid_data_type(s):
    return s in DATA_TYPES


def tok_repr(lx):
    if lx.next_token is EOF:
        return "EOF"
    if lx.next_token in (NAME, BRACKETS, PARENS):
        return lx.token
    return lx.next_token


class Dcl:
    def __init__(self, lexer):
        self.lx = lexer
        self.name = ""
        self.out = ""
        self.error = False
        self.line_nr = 0

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
                self.error = True
                print("Syntax Error: missing ')' on line %d." % self.line_nr)
        elif lx.next_token == NAME:
            self.name = lx.token
        else:
            self.error = True
            print("Syntax Error: expected name or (dcl) on line %d."
                  % self.line_nr)

        while lx.get_next_token() in (PARENS, BRACKETS, PAREN_OPEN):
            if lx.next_token == PAREN_OPEN:
                self.out += " function expecting"
                self.attr_dcl()
                self.out += " and returning"

                if lx.next_token != PAREN_CLOSE:
                    self.error = True
                    print("Syntax Error: missing ')' on line %d."
                          % self.line_nr)
                    if lx.next_token in ("\n", EOF):
                        return
            elif lx.next_token == PARENS:
                self.out += " function returning"
            else:
                self.out += " array[" + lx.token + "] of"

    def attr_dcl(self):
        lx = self.lx
        while lx.get_next_token() not in (PAREN_CLOSE, "\n", EOF):
            if lx.next_token == ATTR_SEPARATOR:
                self.out += ","
            elif lx.next_token == NAME:
                if is_valid_qualifier(lx.token):
                    self.out += " " + lx.token
                    lx.get_next_token()

                if lx.next_token == NAME and is_valid_data_type(lx.token):
                    is_void_type = lx.token == "void"
                    self.out += " " + lx.token

                    lx.get_next_token()
                    if lx.next_token == NAME:
                        if is_void_type:
                            print("Error: variable '%s' has incomplete type "
                                  "'void' on line %d." % (lx.token, self.line_nr))
                        self.out += " " + lx.token
                    elif lx.next_token == PAREN_CLOSE:
                        if is_void_type:
                            return
                        self.error = True
                        print("Syntax Error: missing variable name on line %d."
                              % self.line_nr)
                        return
                    else:
                        self.error = True
                        print("Syntax Error: '%s' unexpected on line %d."
                              % (tok_repr(lx), self.line_nr))
                        if lx.next_token in ("\n", EOF):
                            return
                else:
                    self.error = True
                    print("Syntax Error: '%s' unexpected on line %d."
                          % (tok_repr(lx), self.line_nr))
                    if lx.next_token in (PAREN_CLOSE, "\n", EOF):
                        return
            else:
                self.error = True
                print("Syntax Error: '%s' unexpected on line %d."
                      % (tok_repr(lx), self.line_nr))


def skip_line(lx):
    while lx.next_token not in ("\n", EOF):
        lx.get_next_token()


def main():
    lx = Lexer(sys.stdin.read())
    p = Dcl(lx)

    while lx.get_next_token() is not EOF:
        if lx.next_token == "\n":
            p.line_nr += 1
            continue

        p.out = ""
        p.name = ""

        if lx.next_token == NAME and is_valid_data_type(lx.token):
            data_type = lx.token
        else:
            print("Error: invalid data type '%s' on line %d."
                  % (tok_repr(lx), p.line_nr))
            skip_line(lx)
            p.line_nr += 1
            continue

        p.dcl()

        if lx.next_token != "\n" and lx.next_token is not EOF:
            print("Syntax Error: '%s' unexpected on line %d."
                  % (tok_repr(lx), p.line_nr))
            skip_line(lx)
        elif not p.error:
            print("%s:%s %s" % (p.name, p.out, data_type))

        p.error = False
        p.line_nr += 1


if __name__ == "__main__":
    main()
