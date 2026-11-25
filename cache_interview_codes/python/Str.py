"""
Str: a Python port of the Accelerated C++ `Str` class (Str.h + Str.cpp).

The C++ class manages a raw `char*` buffer. In Python we keep the characters
in a list (mutable, like the char array) and implement the same operators:
    +=, +, comparisons (Q3, Q4), [] access, bool conversion (Q6),
    iteration (Q7), stream output (Q9 -> __str__), getline (Q8),
    operator>> (read_word).
"""
import sys


class Str:
    def __init__(self, *args):
        """
        Str()            -> empty
        Str(n, c)        -> n copies of c
        Str("text")      -> from a string
        Str(other_str)   -> copy constructor
        Str(iterable)    -> from a range of characters
        """
        if len(args) == 0:
            self._value = []
        elif len(args) == 2:
            n, c = args
            self._value = [c] * n
        else:
            src = args[0]
            if isinstance(src, Str):
                self._value = list(src._value)
            else:
                self._value = list(src)

    # ---------- element access ----------
    def __getitem__(self, i):
        return self._value[i]

    def __setitem__(self, i, c):
        self._value[i] = c

    def size(self):
        return len(self._value)

    def __len__(self):
        return len(self._value)

    # ---------- operator+= (Str, char, const char*) ----------
    def __iadd__(self, other):
        if isinstance(other, Str):
            self._value.extend(other._value)
        else:  # char or str (Q5)
            self._value.extend(other)
        return self

    # ---------- operator= (Q11) ----------
    def assign_from(self, rhs):
        if rhs is not self:
            self._value = list(rhs._value)
        return self

    # ---------- Q2 ----------
    def c_str(self):
        return "".join(self._value)

    def data(self):
        return "".join(self._value)

    def copy(self, n):
        """copy the first n characters out (returns them as a list)."""
        return self._value[:n]

    # ---------- Q6 ----------
    def __bool__(self):
        return len(self._value) != 0

    # ---------- Q7 ----------
    def __iter__(self):
        return iter(self._value)

    # ---------- Q9: operator<< ----------
    def __str__(self):
        return self.c_str()

    def __repr__(self):
        return f"Str({self.c_str()!r})"

    # ---------- operator+ (Str+Str, Str+char*, char*+Str: Q5, Q11) ----------
    def __add__(self, other):
        r = Str(self)
        r += other
        return r

    def __radd__(self, other):
        r = Str(other)
        r += self
        return r

    # ---------- Q3 / Q4: comparisons (strcmp semantics) ----------
    @staticmethod
    def _key(x):
        return x.c_str() if isinstance(x, Str) else str(x)

    def __lt__(self, other):
        return self.c_str() < Str._key(other)

    def __gt__(self, other):
        return self.c_str() > Str._key(other)

    def __le__(self, other):
        return self.c_str() <= Str._key(other)

    def __ge__(self, other):
        return self.c_str() >= Str._key(other)

    def __eq__(self, other):
        return self.c_str() == Str._key(other)

    def __ne__(self, other):
        return self.c_str() != Str._key(other)

    __hash__ = None


def read_word(stream, s):
    """
    operator>>(istream&, Str&): skip leading whitespace, then read
    characters until the next whitespace. Returns True on success.
    """
    s._value = []
    c = stream.read(1)
    # read and discard leading whitespace
    while c and c.isspace():
        c = stream.read(1)
    if not c:
        return False
    # read until the next whitespace character
    while c and not c.isspace():
        s += c
        c = stream.read(1)
    return True


def getline(stream, s):
    """Q8: read until newline, appending characters to s."""
    line = stream.readline()
    if not line:
        return False
    s += line.rstrip("\n")
    return True


# small demonstration (Str.cpp itself has no main)
def main():
    s = Str("Hello")
    t = Str(", world!")
    u = s + t
    print(u)
    print("Hey, " + Str("there"))
    print(Str(3, "x"))
    print(f"'abc' < 'abd' ? {Str('abc') < Str('abd')}")
    print(f"'abc' == 'abc' ? {Str('abc') == Str('abc')}")
    print(f"bool(Str()) = {bool(Str())}")
    if not sys.stdin.isatty():
        w = Str()
        while read_word(sys.stdin, w):
            print(f"read word: {w}")


if __name__ == "__main__":
    main()
