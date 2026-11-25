"""
Rule of Three / Rule of Five (port of rule_of_five.cpp).

    Rule Name      Era                  Required Special Functions          Core Purpose
    Rule of Three  C++98 / Traditional  1. Destructor                       Memory safety: deep copies,
                                        2. Copy Constructor                 no double-frees.
                                        3. Copy Assignment
    Rule of Five   C++11 / Modern       All of the above plus:              Performance: steal resources
                                        4. Move Constructor                 from temporaries instead of
                                        5. Move Assignment                  duplicating them.

Python has no implicit copies; we expose each special member explicitly
so the call sequence and messages match the C++ program.
"""


class DynamicBuffer:
    # 0. Standard Constructor
    def __init__(self, s=""):
        self.size = len(s)
        self.data = bytearray(s.encode())
        print(f"[Constructor] Allocated buffer at: {hex(id(self.data))}")

    # 1. DESTRUCTOR
    def __del__(self):
        addr = hex(id(self.data)) if self.data is not None else "0"
        print(f"[Destructor] Freeing buffer at: {addr}")

    # 2. COPY CONSTRUCTOR: deep copy
    @classmethod
    def copy_from(cls, other):
        obj = cls.__new__(cls)
        obj.size = other.size
        obj.data = bytearray(other.data)
        print(f"[Copy Constructor] Deep copied buffer to new address: {hex(id(obj.data))}")
        return obj

    # 3. COPY ASSIGNMENT OPERATOR (copy-and-swap idiom)
    def copy_assign(self, other):
        print("[Copy Assignment] Copying via copy-and-swap")
        if self is not other:
            temp = DynamicBuffer.copy_from(other)       # Make a copy of the source data
            self.data, temp.data = temp.data, self.data  # Swap internal data with temp
            self.size, temp.size = temp.size, self.size
            del temp  # temp goes away, cleaning up our old buffer
        return self

    # 4. MOVE CONSTRUCTOR: "steal" the resource
    @classmethod
    def move_from(cls, other):
        print(f"[Move Constructor] Stealing resources from: {hex(id(other.data))}")
        obj = cls.__new__(cls)
        obj.data = other.data  # Point directly to the existing memory
        obj.size = other.size
        other.data = None      # Null out the source object
        other.size = 0
        return obj

    # 5. MOVE ASSIGNMENT OPERATOR
    def move_assign(self, other):
        print("[Move Assignment] Moving resources")
        if self is not other:
            self.data = other.data  # old buffer released, steal source resource
            self.size = other.size
            other.data = None       # Leave the source in a safe, empty state
            other.size = 0
        return self

    def print(self):
        if self.data:
            print(f"Buffer Content: {self.data.decode()}")
        else:
            print("Buffer Content: [Empty/Moved]")


# main code harness:
def main():
    print("--- 1 & 2: Testing Constructor & Copy Constructor ---")
    b1 = DynamicBuffer("Hello")
    b2 = DynamicBuffer.copy_from(b1)  # Copy Constructor

    print("\n--- 3: Testing Copy Assignment ---")
    b3 = DynamicBuffer("World")
    b3.copy_assign(b1)  # Copy Assignment

    print("\n--- 4: Testing Move Constructor ---")
    b4 = DynamicBuffer.move_from(b2)
    b4.print()
    b2.print()  # b2 is now safely empty

    print("\n--- 5: Testing Move Assignment ---")
    b5 = DynamicBuffer("Temporary")
    b5.move_assign(b3)  # Move Assignment

    print("\n--- Scope Ending: Destructors will clean up remaining objects ---")
    del b5, b4, b3, b2, b1


if __name__ == "__main__":
    main()

# ---------------------------------------------------------------------------
# * Copying: like making a photocopy of a giant binder -- two binders, takes
#   time and paper (memory allocation and deep copying).
# * Moving: like moving the label from your binder to someone else's. The
#   documents never move but ownership changes instantly: O(N) -> O(1).
# ---------------------------------------------------------------------------
