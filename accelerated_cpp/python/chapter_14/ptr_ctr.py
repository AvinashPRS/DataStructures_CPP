# Exercise 14-6: Ptr whose reference count is held by a separate Counter.
from ptr import clone


class Counter:
    def __init__(self, s=1):
        self._refptr = [s]

    def share(self):
        c = Counter.__new__(Counter)
        c._refptr = self._refptr
        return c

    def value(self):
        return self._refptr[0]

    def inc(self):
        self._refptr[0] += 1
        return self

    def dec(self):
        self._refptr[0] -= 1
        return self

    def __eq__(self, other):
        return self.value() == (other.value() if isinstance(other, Counter) else other)


class Ptr:
    def __init__(self, obj=None):
        self._p = obj
        self._ctr = Counter(1)

    def copy(self):
        h = Ptr.__new__(Ptr)
        h._p = self._p
        h._ctr = self._ctr.share()
        h._ctr.inc()
        return h

    __copy__ = copy

    def assign(self, rhs):
        rhs._ctr.inc()
        self._ctr.dec()
        self._p = rhs._p
        self._ctr = rhs._ctr.share()
        return self

    def make_unique(self):
        if self._ctr != 1:
            self._ctr.dec()
            self._ctr = Counter(1)
            self._p = clone(self._p) if self._p is not None else None

    def __bool__(self):
        return self._p is not None

    def get(self):
        if self._p is None:
            raise RuntimeError("unbound Ptr")
        return self._p

    def __eq__(self, other):
        return isinstance(other, Ptr) and self._p is other._p
