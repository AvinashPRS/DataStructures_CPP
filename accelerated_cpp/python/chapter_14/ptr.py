# Ptr<T>: a reference-counted handle with copy-on-write support (§14.3).
# Python already reference-counts objects; the explicit count here mirrors
# the book's design so make_unique() knows when the object is shared.


def clone(obj):
    """§14.4.1/266: delegate to the object's own clone(), falling back to
    a copy for types (like Vec) that lack one (§14.4.1/267)."""
    if hasattr(obj, "clone"):
        return obj.clone()
    import copy
    return copy.copy(obj)


class Ptr:
    def __init__(self, obj=None):
        self._p = obj
        self._refptr = [1]  # shared, mutable reference count

    def copy(self):
        """Copy constructor: share the object and bump the count."""
        h = Ptr.__new__(Ptr)
        h._p = self._p
        h._refptr = self._refptr
        self._refptr[0] += 1
        return h

    __copy__ = copy

    def assign(self, rhs):
        """operator= (§14.2/261)"""
        rhs._refptr[0] += 1
        self._refptr[0] -= 1
        self._p = rhs._p
        self._refptr = rhs._refptr
        return self

    def make_unique(self):
        if self._refptr[0] != 1:
            self._refptr[0] -= 1
            self._refptr = [1]
            self._p = clone(self._p) if self._p is not None else None

    def use_count(self):
        return self._refptr[0]

    def __bool__(self):
        return self._p is not None

    def get(self):
        """operator* / operator->"""
        if self._p is None:
            raise RuntimeError("unbound Ptr")
        return self._p

    def __getattr__(self, name):
        # forward attribute access, like operator->
        if name.startswith("_"):
            raise AttributeError(name)
        return getattr(self.get(), name)

    def __eq__(self, other):
        return isinstance(other, Ptr) and self._p is other._p
