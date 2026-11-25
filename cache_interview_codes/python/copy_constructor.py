"""
Shallow copy vs deep copy (port of copy_constructor.cpp).

In C++, removing the custom copy constructor makes the compiler generate a
SHALLOW copy (`this->buffer = other.buffer`). When the copy is destroyed it
frees the shared buffer, leaving the original with a dangling pointer, and a
double-free happens later.

Python has no manual memory management, so there is no crash. But the same
aliasing problem is visible: a shallow copy shares the same mutable buffer,
so "freeing" (clearing) it through the copy also destroys the original's data.
We simulate `delete[]` by clearing the shared bytearray in the destructor.
"""
import copy


class StringWrapper:
    def __init__(self, s):
        # Regular Constructor: allocate a mutable buffer
        self.buffer = bytearray(s.encode())
        print(f"Object constructed at buffer address: {hex(id(self.buffer))}")

    # --- NO CUSTOM DEEP COPY ---
    # copy.copy() performs a SHALLOW COPY: new.buffer is old.buffer

    def destroy(self):
        """Simulates the C++ destructor: `delete[] buffer`."""
        print(f"Destructor called for buffer address: {hex(id(self.buffer))}")
        self.buffer.clear()  # the shared buffer is "freed"

    def print(self):
        print(f"String value: {self.buffer.decode()}")


def simulateShallowCopyError():
    print("\n=== Starting Simulation ===")

    original = StringWrapper("Hello C++")  # this calls the constructor

    print("\n--- Creating a shallow copy inside an inner block ---")
    cpy = copy.copy(original)  # Default shallow copy occurs here!

    print("Original ", end="")
    original.print()
    print("Copy     ", end="")
    cpy.print()

    print("\n--- Exiting inner block (copy goes out of scope) ---")
    cpy.destroy()  # <-- 'copy' is destroyed here. The shared buffer is "deleted"!

    print("\n--- Back in the outer scope --- ")
    # In C++ this is UNDEFINED BEHAVIOR (dangling pointer).
    # In Python we see the effect: the original's data is gone.
    print("Attempting to access original after copy was destroyed:")
    original.print()

    print("\n=== Exiting Simulation (original goes out of scope) ===")
    original.destroy()  # In C++: double free of the same pointer!


# main code harness:
def main():
    simulateShallowCopyError()


if __name__ == "__main__":
    main()


# ---------------------------------------------------------------------------
# Correct version of the code (deep copy):
#
# class StringWrapper:
#     def __init__(self, s):
#         self.buffer = bytearray(s.encode())
#
#     # Custom Copy Constructor (Deep Copy)
#     def __copy__(self):
#         new = StringWrapper.__new__(StringWrapper)
#         # 1. Allocate brand new memory  2. Copy the actual data
#         new.buffer = bytearray(self.buffer)
#         print("Custom copy constructor called!")
#         return new
#
# obj1 = StringWrapper("Hello C++")
# obj2 = copy.copy(obj1)   # Invokes the deep copy safely
# ---------------------------------------------------------------------------
