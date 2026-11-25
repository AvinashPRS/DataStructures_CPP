# Copy-on-write Str built on Ptr<Vec<char>> (§14.4). The Ptr class is
# injected so the same code serves both Str (exercise 14-5) and
# Str_Ctr (exercise 14-6).
import copy

from _paths import use_chapter

use_chapter(12)
from vec import Vec  # noqa: E402


def make_str_class(PtrClass):
    class Str:
        def __init__(self, *args):
            """Str() | Str(n, c) | Str(text_or_iterable) | Str(other_str)"""
            if len(args) == 2:
                n, c = args
                self._data = PtrClass(Vec(n, c))
            elif args and isinstance(args[0], Str):
                self._data = args[0]._data.copy()  # share until written
            else:
                v = Vec()
                for c in (args[0] if args else ""):
                    v.push_back(c)
                self._data = PtrClass(v)

        def __copy__(self):
            return Str(self)

        def __iadd__(self, other):
            self._data.make_unique()
            if not isinstance(other, Str):
                other = Str(other)
            for c in other._data.get():
                self._data.get().push_back(c)
            return self

        def __add__(self, other):
            r = Str(self)
            r += other
            return r

        def __radd__(self, other):
            r = Str(other)
            r += self
            return r

        def __getitem__(self, i):
            return self._data.get()[i]

        def __setitem__(self, i, c):
            self._data.make_unique()
            self._data.get()[i] = c

        def size(self):
            return self._data.get().size()

        def __iter__(self):
            return iter(self._data.get())

        def __str__(self):
            return "".join(self._data.get())

    return Str


__all__ = ["make_str_class", "copy"]
