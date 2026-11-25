"""
Rule of Five applied to a vector class (port of rule_of_five_vector.cpp).

* Memory Preservation: move constructor / move assignment do zero
  element-wise work -- they hand over a single reference, turning O(N)
  copies into O(1).
* The nullptr clean: the source must be reset after a move so that its
  destructor does not destroy the buffer that was just transferred.
"""


class MyVector:
    # 0. Constructor (with initializer-list support)
    def __init__(self, items):
        self.size = len(items)
        self.capacity = self.size
        self.data = list(items)
        print(f"[Constructor] Allocated array at: {hex(id(self.data))} (Size: {self.size})")

    # 1. DESTRUCTOR
    def __del__(self):
        addr = hex(id(self.data)) if self.data is not None else "0"
        print(f"[Destructor] Freeing array at: {addr}")

    # 2. COPY CONSTRUCTOR: deep copy of the underlying array
    @classmethod
    def copy_from(cls, other):
        obj = cls.__new__(cls)
        obj.size = other.size
        obj.capacity = other.capacity
        obj.data = [other.data[i] for i in range(other.size)]  # Copy one by one
        print(f"[Copy Constructor] Deep copied array to new address: {hex(id(obj.data))}")
        return obj

    # 3. COPY ASSIGNMENT OPERATOR (copy-and-swap)
    def copy_assign(self, other):
        print("[Copy Assignment] Copying via copy-and-swap")
        if self is not other:
            temp = MyVector.copy_from(other)
            self.data, temp.data = temp.data, self.data
            self.size, temp.size = temp.size, self.size
            self.capacity, temp.capacity = temp.capacity, self.capacity
            del temp  # cleans up our old buffer
        return self

    # 4. MOVE CONSTRUCTOR: steal the reference, no element copies
    @classmethod
    def move_from(cls, other):
        print(f"[Move Constructor] Stealing pointer from: {hex(id(other.data))}")
        obj = cls.__new__(cls)
        obj.data = other.data
        obj.size = other.size
        obj.capacity = other.capacity
        # Reset the source vector
        other.data = None
        other.size = 0
        other.capacity = 0
        return obj

    # 5. MOVE ASSIGNMENT OPERATOR
    def move_assign(self, other):
        print("[Move Assignment] Moving array pointers")
        if self is not other:
            self.data = other.data
            self.size = other.size
            self.capacity = other.capacity
            other.data = None
            other.size = 0
            other.capacity = 0
        return self

    def print(self):
        if not self.data or self.size == 0:
            print("Vector: [Empty/Moved]")
            return
        print("Vector elements: [ " + "".join(f"{x} " for x in self.data[:self.size]) + "]")


# main code harness:
def main():
    print("--- 1 & 2: Testing Constructor & Copy Constructor ---")
    v1 = MyVector([10, 20, 30])
    v2 = MyVector.copy_from(v1)  # Copy Constructor

    print("\n--- 3: Testing Copy Assignment ---")
    v3 = MyVector([99, 100])
    v3.copy_assign(v1)  # Copy Assignment

    print("\n--- 4: Testing Move Constructor ---")
    v4 = MyVector.move_from(v2)
    v4.print()
    v2.print()  # v2 is now empty

    print("\n--- 5: Testing Move Assignment ---")
    v5 = MyVector([4, 5, 6])
    v5.move_assign(v3)  # Move Assignment
    v5.print()

    print("\n--- Scope Ending: Destructors will clean up remaining objects ---")
    del v5, v4, v3, v2, v1


if __name__ == "__main__":
    main()
