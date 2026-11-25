# A tiny stand-in for std::istream's `>>` operator on whitespace-separated
# input, so the class-based chapters can keep their `read(stream)` style.
import sys


class TokenStream:
    def __init__(self, source=None):
        if source is None:
            source = sys.stdin
        text = source if isinstance(source, str) else source.read()
        self._tokens = text.split()
        self._pos = 0
        self.ok = True

    def __bool__(self):
        return self.ok

    def peek(self):
        return self._tokens[self._pos] if self._pos < len(self._tokens) else None

    def word(self):
        tok = self.peek()
        if tok is None:
            self.ok = False
            return ""
        self._pos += 1
        return tok

    def number(self):
        tok = self.peek()
        try:
            value = float(tok)
        except (TypeError, ValueError):
            self.ok = False
            return 0.0
        self._pos += 1
        return value

    def numbers(self):
        """Read numbers until a non-number or end of input (like read_hw)."""
        values = []
        while True:
            tok = self.peek()
            try:
                values.append(float(tok))
            except (TypeError, ValueError):
                return values
            self._pos += 1
