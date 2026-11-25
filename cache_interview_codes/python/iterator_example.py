"""
Iterating over nested containers (port of iterator_example.cpp).

In C++ the iterators outerIt/innerIt behave like pointers; on a 64-bit
system they are 8 bytes, on a 32-bit system 4 bytes.

    Target Architecture    Address Bus  Raw Pointer  outerIt  innerIt
    32-bit (x86 / ARM32)   32 bits      4 bytes      4 bytes  4 bytes
    64-bit (x64 / ARM64)   64 bits      8 bytes      8 bytes  8 bytes

In Python, iterators are full objects; their size is reported by
sys.getsizeof and pointer size can be obtained via ctypes.
"""
import ctypes
import sys


# main code harness:
def main():
    # A list containing lists of strings
    grid = [
        ["Apple", "Banana", "Cherry"],
        ["Dog", "Elephant"],
        ["C++", "Java", "Python", "Go"],
    ]

    # 1. Explicit iterator syntax (like the traditional C++ way)
    print("--- Using Explicit Iterators ---")
    outerIt = iter(grid)
    for row in outerIt:
        innerIt = iter(row)
        for item in innerIt:
            print(item, end=" ")
        print()

    # 2. Idiomatic Python (like the modern C++ auto / range-for)
    print("\n--- Using for-in (idiomatic) ---")
    for row in grid:
        for item in row:
            print(item, end=" ")
        print()

    # Also what would be the size of the iterators/pointers:
    print(f"Outer iterator size: {sys.getsizeof(iter(grid))} bytes")
    print(f"Inner iterator size: {sys.getsizeof(iter(grid[0]))} bytes")
    print(f"Raw pointer size:    {ctypes.sizeof(ctypes.c_void_p)} bytes")


if __name__ == "__main__":
    main()
