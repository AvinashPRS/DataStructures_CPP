"""
Vec: a Python port of the Accelerated C++ `Vec<T>` class (Vec.h / Vec.cpp).

The C++ version manages raw memory with std::allocator using three pointers:
    data  -> first element
    avail -> one past the last constructed element
    limit -> one past the allocated memory

Python has no raw memory, so we emulate the buffer with a fixed-size list
(`_buf`) plus integer indices `_avail` and `_limit`. "Iterators" are plain
integer indices into the buffer. Capacity doubles on growth, exactly as in
the C++ grow().
"""


class Vec:
    # ---------------- constructors / copy control ----------------
    def __init__(self, *args):
        """
        Vec()                 -> empty
        Vec(n, val=None)      -> n copies of val
        Vec(other_vec)        -> copy constructor
        Vec(iterable)         -> range constructor (Q10)
        """
        if len(args) == 0:
            self._create()
        elif len(args) <= 2 and isinstance(args[0], int):
            n = args[0]
            val = args[1] if len(args) == 2 else None
            self._create_fill(n, val)
        elif len(args) == 1 and isinstance(args[0], Vec):
            self._create_range(list(args[0]))
        elif len(args) == 1:
            self._create_range(list(args[0]))
        else:
            raise TypeError("invalid Vec constructor arguments")

    def assign_from(self, rhs):
        """operator=(const Vec&) -- copy assignment."""
        # check for self-assignment
        if rhs is not self:
            # free the array in the left-hand side
            self._uncreate()
            # copy elements from the right-hand to the left-hand side
            self._create_range(list(rhs))
        return self

    def copy(self):
        return Vec(self)

    # ---------------- element access ----------------
    def __getitem__(self, i):
        if not 0 <= i < self._avail:
            raise IndexError("Vec index out of range")
        return self._buf[i]

    def __setitem__(self, i, val):
        if not 0 <= i < self._avail:
            raise IndexError("Vec index out of range")
        self._buf[i] = val

    def push_back(self, val):
        if self._avail == self._limit:
            self._grow()
        self._unchecked_append(val)

    def size(self):
        return self._avail

    def capacity(self):
        return self._limit

    def __len__(self):
        return self._avail

    # iterators are indices
    def begin(self):
        return 0

    def end(self):
        return self._avail

    def __iter__(self):
        for i in range(self._avail):
            yield self._buf[i]

    def clear(self):
        self._uncreate()

    def empty(self):
        return self._avail == 0

    def erase(self, pos, last=None):
        """
        erase(pos)         -> remove element at index pos
        erase(first, last) -> remove elements in [first, last)
        Returns the index of the element following the erased range.
        """
        if last is None:
            last = pos + 1
        items = [self._buf[i] for i in range(self._avail) if not (pos <= i < last)]
        self._uncreate()
        self._create_range(items)
        return pos

    def insert(self, d, src_iterable):
        """Q12: insert the elements of src_iterable before index d."""
        items = list(src_iterable)  # copy first, in case src is self
        # save the tail and the difference
        tail = [self._buf[i] for i in range(d, self._avail)]
        diff = d

        # destroy the tail
        for i in range(d, self._avail):
            self._buf[i] = None
        self._avail = d

        # insert the items
        for x in items:
            self.push_back(x)

        # add the tail
        for x in tail:
            self.push_back(x)

        return diff

    def assign(self, src_iterable):
        """Q13: replace contents with the elements of src_iterable."""
        items = list(src_iterable)
        # destroy the Vec
        self._uncreate()
        # push all the elements denoted by the iterators
        for x in items:
            self.push_back(x)

    def __repr__(self):
        return f"Vec({list(self)})"

    # ---------------- memory management helpers ----------------
    def _create(self):
        self._buf = []
        self._avail = 0
        self._limit = 0

    def _create_fill(self, n, val):
        self._buf = [val] * n
        self._avail = self._limit = n

    def _create_range(self, items):
        self._buf = list(items)
        self._avail = self._limit = len(items)

    def _uncreate(self):
        # destroy (in reverse order) the elements that were constructed
        # and return all the space -- Python's GC does the real work.
        self._buf = []
        self._avail = self._limit = 0

    def _grow(self):
        # when growing, allocate twice as much space as currently in use
        new_size = max(2 * self._limit, 1)
        # allocate new space and copy existing elements to the new space
        new_buf = [None] * new_size
        new_buf[:self._avail] = self._buf[:self._avail]
        new_avail = self._avail
        # return the old space
        self._uncreate()
        # reset "pointers" to point to the newly allocated space
        self._buf = new_buf
        self._avail = new_avail
        self._limit = new_size

    def _unchecked_append(self, val):
        # assumes avail points at allocated, but uninitialized space
        self._buf[self._avail] = val
        self._avail += 1


# ============================================================================
# Helper function to easily print the elements of our custom Vec
# ============================================================================
def printVec(label, v):
    print(f"{label}: [ " + "".join(f"{x} " for x in v) + f"] (Size: {v.size()})")


# main code harness:
def main():
    print("=== Testing Vec Constructors & push_back ===")

    # 1. Test Default Constructor
    v1 = Vec()
    print(f"v1 empty? {'Yes' if v1.empty() else 'No'}")

    # 2. Test push_back (triggers grow internally)
    v1.push_back(10)
    v1.push_back(20)
    v1.push_back(30)
    printVec("v1 after push_back", v1)

    # 3. Sized constructor
    v2 = Vec(4, 99)
    printVec("v2 (sized constructor with default values)", v2)

    # 4. Test Copy Constructor
    v3 = Vec(v1)
    printVec("v3 (copied from v1)", v3)

    print("\n=== Testing Assignment and Operators ===")

    # 5. Test Copy Assignment Operator (=)
    v2.assign_from(v1)
    printVec("v2 (after v2 = v1 assignment)", v2)

    # 6. Test Subscript Operator ([]) and element mutation
    v1[0] = 55
    print(f"v1[0] modified to: {v1[0]}")
    printVec("v1 modified", v1)
    printVec("v2 unchanged (deep copy verification)", v2)

    print("\n=== Testing Custom Iterator Methods (insert & assign) ===")

    # 7. Test range-based Constructor (Q10)
    arr = [1, 2, 3, 4, 5]
    v4 = Vec(arr)
    printVec("v4 initialized from raw array pointers", v4)

    # 8. Test custom insert function (Q12)
    print("Inserting elements into v4...")
    v4.insert(v4.begin() + 2, v1)
    printVec("v4 after inserting v1 at index 2", v4)

    # 9. Test assign function (Q13)
    print("Re-assigning values to v1...")
    v1.assign(arr[:3])
    printVec("v1 after assigning first 3 elements of raw array", v1)

    # 10. Test clear functionality
    v1.clear()
    print(f"v1 after clear(). Is empty? {'Yes' if v1.empty() else 'No'}")


if __name__ == "__main__":
    main()
