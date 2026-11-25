# Str implemented on top of Vec<char> (exercises 12-10 and 12-12).
from vec import Vec


class Str:
    def __init__(self, *args):
        """Str() | Str(n, c) | Str(text_or_iterable)"""
        if not args:
            self._data = Vec()
        elif len(args) == 2:
            n, c = args
            self._data = Vec(n, c)
        else:
            self._data = Vec(iterable=args[0])

    def __getitem__(self, i):
        if isinstance(i, slice):  # Str(&s[0], &s[5]) becomes s[0:5]
            return [self._data[k] for k in range(*i.indices(self.size()))]
        return self._data[i]

    def size(self):
        return self._data.size()

    def __iadd__(self, other):
        for c in other:
            self._data.push_back(c)
        return self

    def __add__(self, other):
        r = Str(self)
        r += other
        return r

    def __iter__(self):
        return iter(self._data)

    def insert(self, d, items):
        return self._data.insert(d, items)

    def __str__(self):
        return "".join(self._data)
