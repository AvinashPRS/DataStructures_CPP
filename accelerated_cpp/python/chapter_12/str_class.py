# Str: a string class that manages its own character array (chapter 12).
import sys
from functools import total_ordering


@total_ordering
class Str:
    def __init__(self, *args):
        """Str() | Str(n, c) | Str(text) | Str(other_str) | Str(iterable_of_chars)"""
        if not args:
            chars = []
        elif len(args) == 2:
            n, c = args
            chars = [c] * n
        else:
            src = args[0]
            chars = list(src._value) if isinstance(src, Str) else list(src)
        self._value = chars

    # --- element access ---------------------------------------------------
    def __getitem__(self, i):
        return self._value[i]

    def __setitem__(self, i, c):
        self._value[i] = c

    def size(self):
        return len(self._value)

    def __len__(self):
        return len(self._value)

    def __iter__(self):  # exercise 12-7: iterators
        return iter(self._value)

    # --- concatenation (§12.3.3, exercises 12-5 and 12-11) ----------------
    def __iadd__(self, other):
        if isinstance(other, Str):
            other = other._value
        self._value = self._value + list(other)
        return self

    def __add__(self, other):
        r = Str(self)
        r += other
        return r

    def __radd__(self, other):  # "text" + Str
        r = Str(other)
        r += self
        return r

    # --- exercise 12-2: c_str, data, copy ---------------------------------
    def c_str(self):
        return "".join(self._value)

    def data(self):
        return "".join(self._value)

    def copy(self, n):
        return self._value[:n]

    # --- exercise 12-6: truth value ---------------------------------------
    def __bool__(self):
        return len(self._value) != 0

    # --- exercises 12-3 / 12-4: comparisons ------------------------------
    def __eq__(self, other):
        return isinstance(other, Str) and self._value == other._value

    def __lt__(self, other):
        return self._value < other._value

    def __hash__(self):
        return hash(self.c_str())

    # --- exercise 12-9: output --------------------------------------------
    def __str__(self):
        return "".join(self._value)

    def __repr__(self):
        return f"Str({self.c_str()!r})"


class CharStream:
    """Character-level input stream for operator>> and getline."""

    def __init__(self, source=None):
        source = sys.stdin if source is None else source
        self._text = source if isinstance(source, str) else source.read()
        self._pos = 0
        self.ok = True

    def __bool__(self):
        return self.ok

    def get(self):
        if self._pos >= len(self._text):
            self.ok = False
            return None
        c = self._text[self._pos]
        self._pos += 1
        return c

    def unget(self):
        self._pos -= 1


def read_word(stream, s):
    """operator>>: read one whitespace-delimited word into s."""
    s._value = []
    c = stream.get()
    while c is not None and c.isspace():
        c = stream.get()
    if stream:
        while c is not None and not c.isspace():
            s += c
            c = stream.get()
        if stream:
            stream.unget()
    return stream


def getline(stream, s):
    """Exercise 12-8: read characters into s until a newline."""
    c = stream.get()
    while c is not None and c != "\n":
        s += c
        c = stream.get()
    return stream
