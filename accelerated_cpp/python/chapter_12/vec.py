# Vec<T> from chapter 11 with the chapter 12 additions (insert, assign).
# Storage is a fixed-size Python list; `_avail` is the number of
# constructed elements and len(self._data) plays the role of `limit`.


class Vec:
    def __init__(self, n=0, value=None, iterable=None):
        if iterable is not None:
            self._create_from(list(iterable))
        else:
            self._data = [value] * n
            self._avail = n

    # --- §11.5.1 memory management helpers -------------------------------
    def _create_from(self, items):
        self._data = list(items)
        self._avail = len(items)

    def _uncreate(self):
        self._data = []
        self._avail = 0

    def _grow(self):
        """Allocate twice as much space as currently in use."""
        new_size = max(2 * len(self._data), 1)
        self._reallocate(new_size)

    def _grow_once(self):
        """Exercise 11-9: grow by just one element each time."""
        self._reallocate(len(self._data) + 1)

    def _reallocate(self, new_size):
        new_data = [None] * new_size
        new_data[:self._avail] = self._data[:self._avail]
        self._data = new_data

    def _unchecked_append(self, value):
        self._data[self._avail] = value
        self._avail += 1

    # --- public interface -------------------------------------------------
    def push_back(self, value):
        if self._avail == len(self._data):
            self._grow()
        self._unchecked_append(value)

    def push_back_grow_once(self, value):
        self._grow_once()
        self._unchecked_append(value)

    def size(self):
        return self._avail

    def __len__(self):
        return self._avail

    def empty(self):
        return self._avail == 0

    def clear(self):
        self._uncreate()

    def erase(self, pos, end=None):
        """Erase element `pos`, or the range [pos, end). Returns the index
        of the element following the erased ones."""
        if end is None:
            end = pos + 1
        if not 0 <= pos <= end <= self._avail:
            raise IndexError("erase range out of bounds")
        kept = self._data[:pos] + self._data[end:self._avail]
        self._create_from(kept)
        return pos

    def assign(self, rhs):
        """operator= (§11.3.2/197)"""
        if rhs is not self:
            self._uncreate()
            self._create_from(rhs._data[:rhs._avail])
        return self

    def __copy__(self):
        return Vec(iterable=self)

    def __getitem__(self, i):
        if not 0 <= i < self._avail:
            raise IndexError(i)
        return self._data[i]

    def __setitem__(self, i, value):
        if not 0 <= i < self._avail:
            raise IndexError(i)
        self._data[i] = value

    def __iter__(self):
        for i in range(self._avail):
            yield self._data[i]

    def sort(self, key=None):
        self._data[:self._avail] = sorted(self._data[:self._avail], key=key)

    # --- additions for chapter 12 -----------------------------------------
    def insert(self, d, items):
        """Exercise 12-12: insert `items` before index d; return d."""
        tail = self._data[d:self._avail]
        self._avail = d
        for x in items:
            self.push_back(x)
        for x in tail:
            self.push_back(x)
        return d

    def assign_range(self, items):
        """Exercise 12-13: replace the contents with `items`."""
        self._uncreate()
        for x in items:
            self.push_back(x)
