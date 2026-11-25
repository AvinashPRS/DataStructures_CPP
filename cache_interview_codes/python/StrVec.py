"""
StrVec: a vector of strings with manual capacity management
(port of StrVec.cpp, from C++ Primer chapter 13). Compare with Vec.py.

C++ concepts and how they map here:
  * allocator / elements / first_free / cap  -> list buffer + size + capacity
  * copy constructor / copy assignment       -> StrVec.copy() / assign_copy()
  * move constructor / move assignment       -> StrVec.move_from() / assign_move()
    (moving steals the buffer and leaves the source empty, just like C++)
"""


class StrVec:
    # Constructors
    def __init__(self, init=None):
        """StrVec() or StrVec(["a", "b", ...]) (initializer-list constructor)."""
        self._elements = None   # underlying buffer
        self._first_free = 0    # index of first free element
        self._cap = 0           # allocated capacity
        if init is not None:
            data, n = self._alloc_n_copy(list(init))
            self._elements = data
            self._first_free = self._cap = n

    # Copy constructor
    @classmethod
    def copy(cls, s):
        v = cls()
        data, n = v._alloc_n_copy(list(s))
        v._elements = data
        v._first_free = v._cap = n
        return v

    # Move constructor
    @classmethod
    def move_from(cls, s):
        v = cls()
        v._elements, v._first_free, v._cap = s._elements, s._first_free, s._cap
        # Leave s in a state where it is safe to destroy
        s._elements, s._first_free, s._cap = None, 0, 0
        return v

    # Copy assignment
    def assign_copy(self, rhs):
        data, n = self._alloc_n_copy(list(rhs))
        self._free()
        self._elements = data
        self._first_free = self._cap = n
        return self

    # Move assignment
    def assign_move(self, rhs):
        # Direct protection against self-assignment
        if self is not rhs:
            self._free()  # Get rid of existing elements
            self._elements, self._first_free, self._cap = rhs._elements, rhs._first_free, rhs._cap
            rhs._elements, rhs._first_free, rhs._cap = None, 0, 0
        return self

    # Public member functions
    def push_back(self, s):
        self._chk_n_alloc()  # Ensure space exists
        self._elements[self._first_free] = s
        self._first_free += 1

    def size(self):
        return self._first_free

    def capacity(self):
        return self._cap

    def __iter__(self):
        for i in range(self._first_free):
            yield self._elements[i]

    # Subscript operators
    def __getitem__(self, n):
        return self._elements[n]

    def __setitem__(self, n, val):
        self._elements[n] = val

    # ---- utilities used by the copy-control members ----
    def _chk_n_alloc(self):
        if self.size() == self.capacity():
            self._reallocate()

    @staticmethod
    def _alloc_n_copy(items):
        """Allocate space and copy a range: returns (buffer, count)."""
        return list(items), len(items)

    def _free(self):
        """Destroy elements and deallocate space."""
        self._elements = None
        self._first_free = self._cap = 0

    def _reallocate(self):
        """Get more space (doubling strategy) and move existing elements."""
        newcapacity = 2 * self.size() if self.size() else 1
        first = [None] * newcapacity

        # Move elements from old space to new space
        n = self.size()
        for i in range(n):
            first[i] = self._elements[i]

        self._free()  # Free old space now that items are moved

        # Update data structures to point to new space
        self._elements = first
        self._first_free = n
        self._cap = newcapacity


# Helper function to print the current state of a StrVec
def printVec(label, vec):
    elems = "".join(f'"{s}" ' for s in vec)
    print(f"{label} | Size: {vec.size()}, Capacity: {vec.capacity()} | Elements: [ {elems}]")


# main code harness:
def main():
    print("--- 1. Testing Default Constructor & push_back ---")
    vec1 = StrVec()
    printVec("vec1 (init)", vec1)

    # Testing dynamic reallocation (doubling strategy)
    vec1.push_back("Hello")
    vec1.push_back("World")
    vec1.push_back("C++")
    vec1.push_back("Primer")
    printVec("vec1 (after push_backs)", vec1)

    print("\n--- 2. Testing Initializer List Constructor ---")
    vec2 = StrVec(["Barbara", "Moo", "Stanley", "Lippman"])
    printVec("vec2", vec2)

    print("\n--- 3. Testing Copy Semantics (Deep Copy) ---")
    vec3 = StrVec.copy(vec2)  # Copy constructor
    vec3[0] = "Dr."           # Modify copy to prove independence
    printVec("vec2 (original)", vec2)
    printVec("vec3 (copied & mutated)", vec3)

    print("\n--- 4. Testing Move Semantics (Resource Transfer) ---")
    printVec("vec1 before move", vec1)

    # Move constructor
    vec4 = StrVec.move_from(vec1)
    print(">> Moved vec1 into vec4")
    printVec("vec4 (destination)", vec4)
    printVec("vec1 (source - now safe/empty)", vec1)

    print("\n--- 5. Testing Assignment Operators ---")
    vec5 = StrVec()
    vec5.assign_copy(vec2)  # Copy assignment
    printVec("vec5 (after copy assignment)", vec5)

    vec6 = StrVec()
    vec6.assign_move(vec2)  # Move assignment
    print(">> Move assigned vec2 into vec6")
    printVec("vec6 (destination)", vec6)
    printVec("vec2 (source - now safe/empty)", vec2)


if __name__ == "__main__":
    main()


# ---------------------------------------------------------------------------
# The C++ file also had (commented out) a CustomContainer example showing an
# initializer_list constructor. Python equivalent:
#
# class CustomContainer:
#     def __init__(self, items):
#         self.data = list(items)
#         print(f"Constructed with {len(self.data)} elements.")
#
#     def print(self):
#         print(" ".join(str(v) for v in self.data))
#
# CustomContainer([10, 20, 30, 40]).print()   # Output: 10 20 30 40
# ---------------------------------------------------------------------------
