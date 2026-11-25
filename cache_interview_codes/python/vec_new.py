"""
A minimal Vec<T> (port of vec_new.cpp).

The C++ version uses std::allocator, uninitialized_fill/copy and three pointers
(data, avail, limit). Here the raw buffer is a Python list of fixed capacity and
the "pointers" are integer indices.
"""


class Vec:
    # Constructors, Copy Control
    def __init__(self, *args):
        """
        Vec()          -> empty
        Vec(n, val)    -> fill constructor (uses 'uninitialized_fill')
        Vec(other)     -> copy constructor (uses 'uninitialized_copy')
        """
        if not args:
            self._create()
        elif isinstance(args[0], Vec):
            self._create_range(args[0])
        else:
            n = args[0]
            val = args[1] if len(args) > 1 else None
            self._create_fill(n, val)

    def assign_from(self, rhs):
        """Assignment operator."""
        # Check for self-assignment
        if rhs is not self:
            # Free the array in the left-hand side
            self._uncreate()
            # Copy elements from the right-hand side to the left-hand side
            self._create_range(rhs)
        return self

    # Element access
    def __getitem__(self, i):
        return self._data[i]

    def __setitem__(self, i, val):
        self._data[i] = val

    # Mutators and capacity
    def push_back(self, val):
        if self._avail == self._limit:
            self._grow()
        self._unchecked_append(val)

    def size(self):
        return self._avail

    # Iterators
    def __iter__(self):
        return iter(self._data[:self._avail])

    def clear(self):
        self._uncreate()

    # ---- private helpers ----

    # 1. Default create: empty Vec
    def _create(self):
        self._data = []
        self._avail = self._limit = 0

    # 2. Fill create
    def _create_fill(self, n, val):
        self._data = [val] * n
        self._limit = self._avail = n

    # 3. Range create
    def _create_range(self, other):
        self._data = list(other)
        self._limit = self._avail = len(self._data)

    # Destroy elements and deallocate buffer
    def _uncreate(self):
        # Reset to indicate that the Vec is empty again
        self._data = []
        self._avail = self._limit = 0

    # Reallocate with double capacity when avail == limit
    def _grow(self):
        # When growing, allocate twice as much space as currently in use
        new_size = max(2 * self._limit, 1)

        # Allocate new space and copy existing elements to the new space
        new_data = [None] * new_size
        new_data[:self._avail] = self._data[:self._avail]
        new_avail = self._avail

        # Return the old space
        self._uncreate()

        # Reset to point to the newly allocated space
        self._data = new_data
        self._avail = new_avail
        self._limit = new_size

    # Construct a single element at avail (assumes allocated space exists)
    def _unchecked_append(self, val):
        self._data[self._avail] = val
        self._avail += 1


def print_vec(label, v):
    print(f"{label} (size={v.size()}): [ " + "".join(f"{x} " for x in v) + "]")


# main code harness:
def main():
    # 1. Default constructor (empty Vec)
    v1 = Vec()
    print_vec("1. Default constructor", v1)

    # 2. push_back() -> triggers grow() and unchecked_append()
    v1.push_back("Alpha")
    v1.push_back("Beta")
    v1.push_back("Gamma")
    print_vec("2. After push_back", v1)

    # 3. Fill constructor Vec(n, val)
    v2 = Vec(4, "Init")
    print_vec("3. Fill constructor", v2)

    # 4. Copy constructor Vec(const Vec&)
    v3 = Vec(v1)
    print_vec("4. Copy constructor (v3 from v1)", v3)

    # 5. Index access operator[]
    v3[1] = "Modified"
    print(f"5. v3[1] after modification: {v3[1]}")
    print_vec("   v1 remains unchanged", v1)

    # 6. Copy assignment operator= -> calls uncreate() then create()
    v2.assign_from(v3)
    print_vec("6. Copy assignment (v2 = v3)", v2)

    # 7. Self-assignment check
    v2.assign_from(v2)
    print_vec("7. After self-assignment (v2 = v2)", v2)

    # 8. Clear -> calls uncreate()
    v2.clear()
    print_vec("8. After v2.clear()", v2)


if __name__ == "__main__":
    main()
