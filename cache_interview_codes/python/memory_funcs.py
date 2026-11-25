"""
Raw-memory algorithms and erase patterns (port of memory_funcs.cpp).

C++ uses std::allocator + uninitialized_fill / uninitialized_copy / destroy
on raw buffers. Python has no uninitialized memory, so a "raw buffer" is a
list of `None` slots of the allocated capacity; "constructing" writes values
into slots and "destroying" resets them to None. Indices play the role of
pointers.
"""


def print_range(label, buf, begin, end):
    print(f"{label}: [ " + "".join(f"{buf[i]} " for i in range(begin, end)) + "]")


def allocate(n):
    """alloc.allocate(n): raw, uninitialized storage."""
    return [None] * n


def destroy(buf, first, last):
    """std::destroy(first, last)."""
    for i in range(first, last):
        buf[i] = None


def move_range(buf, first, last, d_first):
    """
    std::move(first, last, d_first) on the same buffer (shift left).
    Moved-from slots become "" (valid but unspecified, like std::string).
    Returns the new end index (d_first + count).
    """
    for i in range(first, last):
        buf[d_first] = buf[i]
        buf[i] = ""
        d_first += 1
    return d_first


# main code harness:
def main():
    # =========================================================================
    # 1. uninitialized_fill & Full-Range Erase (destroy)
    # =========================================================================
    size = 3
    buffer = allocate(size)
    for i in range(size):
        buffer[i] = "Init"
    print_range("1. uninitialized_fill", buffer, 0, size)
    # Erase full range (reverts memory back to uninitialized state)
    destroy(buffer, 0, size)

    # =========================================================================
    # 2. uninitialized_fill_n & Count-Based Erase (destroy_n)
    # =========================================================================
    capacity, count = 5, 3
    buffer = allocate(capacity)
    for i in range(count):
        buffer[i] = "Item"
    end_ptr = count
    print_range("2. uninitialized_fill_n", buffer, 0, end_ptr)
    destroy(buffer, 0, count)

    # =========================================================================
    # 3. uninitialized_copy & Middle Element Erase (move + destroy_at)
    # =========================================================================
    src = ["Alpha", "Beta", "Gamma"]
    buffer = allocate(len(src))
    buffer[:len(src)] = src
    end_ptr = len(src)
    print_range("3a. uninitialized_copy", buffer, 0, end_ptr)

    # Erase "Beta" at index 1
    pos = 1
    new_end = move_range(buffer, pos + 1, end_ptr, pos)  # Shift left
    buffer[new_end] = None                               # Destroy trailing slot
    end_ptr = new_end
    print_range("3b. After middle erase", buffer, 0, end_ptr)
    destroy(buffer, 0, end_ptr)

    # =========================================================================
    # 4. uninitialized_copy_n & Prefix Erase (move + destroy)
    # =========================================================================
    src = ["One", "Two", "Three", "Four"]
    copy_count = 4
    buffer = allocate(copy_count)
    buffer[:copy_count] = src[:copy_count]
    end_ptr = copy_count
    print_range("4a. uninitialized_copy_n", buffer, 0, end_ptr)

    # Erase first 2 elements ("One", "Two")
    erase_count = 2
    new_end = move_range(buffer, erase_count, end_ptr, 0)
    destroy(buffer, new_end, end_ptr)  # Destroy vacated slots at the end
    end_ptr = new_end
    print_range("4b. After prefix erase", buffer, 0, end_ptr)
    destroy(buffer, 0, end_ptr)

    # =========================================================================
    # 5. uninitialized_move & Pop Back Erase (destroy_at)
    # =========================================================================
    src = ["LargeString1", "LargeString2"]
    buffer = allocate(len(src))
    for i in range(len(src)):
        buffer[i] = src[i]
        src[i] = ""  # moved-from
    end_ptr = len(buffer)
    print_range("5a. uninitialized_move", buffer, 0, end_ptr)

    # Pop back ("LargeString2")
    end_ptr -= 1
    buffer[end_ptr] = None
    print_range("5b. After pop_back", buffer, 0, end_ptr)
    destroy(buffer, 0, end_ptr)

    # -------------------------------------------------------------------------
    # To erase a subrange [first, last) from the middle of an initialized raw
    # buffer, combine move (shift the trailing elements left over the erased
    # gap) with destroy (destroy the leftover trailing elements at the old end).
    #
    # Breakdown of the Math
    #  * Original Active Count: 6 elements (index 0..5), so end_ptr = 6.
    #  * Erased Subrange [first, last): first = 2 ("C"), last = 5 ("F").
    #    That is 5 - 2 = 3 elements erased.
    #  * Elements Shifted: move(last, end_ptr, first) takes the 1 remaining
    #    element in [last, end_ptr) ("F" at index 5) and moves it into index 2.
    #  * Resulting new_end: first + 1 = 3.
    #
    # new_end is the dividing line between surviving data [0, 3) = A B F and
    # the leftover objects [3, 6) = D, E, "" that must be destroyed.
    # -------------------------------------------------------------------------
    src = ["A", "B", "C", "D", "E", "F"]
    buffer = allocate(len(src))

    # 1. Construct initial elements in raw memory
    buffer[:] = src
    end_ptr = len(src)
    print_range("Before range erase", buffer, 0, end_ptr)

    # 2. Define the half-open subrange [first, last) to erase: {"C", "D", "E"}
    first = 2  # "C"
    last = 5   # "F" (one past "E")

    # 3. Shift elements after 'last' ("F") down to 'first'
    new_end = move_range(buffer, last, end_ptr, first)

    # 4. Destroy the leftover moved-from objects in [new_end, end_ptr)
    destroy(buffer, new_end, end_ptr)

    # 5. Update logical end
    end_ptr = new_end
    print_range("After range erase ", buffer, 0, end_ptr)

    # 6. Final cleanup
    destroy(buffer, 0, end_ptr)

    # -------------------------------------------------------------------------
    # Some more list erases (std::vector::erase equivalents)
    # Capacity is unchanged in C++; in Python lists may shrink internally.
    # -------------------------------------------------------------------------

    # 1. Erasing a Single Element (vec.erase(pos))
    vec = ["Alpha", "Beta", "Gamma", "Delta"]
    idx = 1
    del vec[idx]  # Erase "Beta" at index 1
    print(f"Returned iterator points to: {vec[idx]}")  # Output: Gamma
    print(" ".join(vec) + " ")                          # Output: Alpha Gamma Delta

    # 2. Erasing a Range (vec.erase(first, last))
    vec1 = ["A", "B", "C", "D", "E", "F"]
    first1, last1 = 2, 5
    del vec1[first1:last1]  # Erase {"C", "D", "E"}
    print(f"Returned iterator points to: {vec1[first1]}")  # Output: F
    # (the C++ original printed `vec` here by mistake; we print it the same way)
    print(" ".join(vec) + " ")

    # 3. Erasing While Looping (Safe Iterator Pattern)
    nums = [1, 2, 3, 4, 5, 6]
    i = 0
    while i < len(nums):
        if nums[i] % 2 == 0:
            del nums[i]  # next element shifts into position i
        else:
            i += 1
    # (idiomatic Python: nums = [n for n in nums if n % 2 != 0])
    print(" ".join(str(n) for n in nums) + " ")  # Output: 1 3 5


if __name__ == "__main__":
    main()
