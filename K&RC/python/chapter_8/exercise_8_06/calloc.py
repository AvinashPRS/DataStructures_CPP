"""Exercise 8-6: calloc(n, size) returns a pointer to n objects of size
size, with the storage initialized to zero, built on top of malloc.

Memory, headers and pointers are simulated (see the comment below).
"""
import sys

MIN_NR_OF_UNITS = 1024
HEADER_SIZE = 16  # sizeof(Header): one pointer + one size_t

# --------------------------------------------------------------------------
# Python has no raw pointers, so memory is simulated: `memory` is a bytearray
# acting as the heap (grown by sbrk) and a "pointer" is an index of a unit of
# HEADER_SIZE bytes. Each block header (free_block_p, size) is stored in the
# dictionaries below, keyed by the unit index of the header.
# Unit 0 is the static `base` header of the free list.
# --------------------------------------------------------------------------
memory = bytearray(HEADER_SIZE)  # unit 0 = base
next_free = {}   # header unit -> unit of next free block (s.free_block_p)
size = {}        # header unit -> size of block in units (s.size)

BASE = 0
free_p = None


def sbrk(nr_of_bytes):
    """Grow the simulated heap; return the unit index of the new region."""
    start = len(memory) // HEADER_SIZE
    memory.extend(bytes(nr_of_bytes))
    return start


def strcpy(p, s):
    data = s.encode() + b"\0"
    off = p * HEADER_SIZE
    memory[off:off + len(data)] = data


def string_at(p):
    off = p * HEADER_SIZE
    end = memory.index(0, off)
    return memory[off:end].decode()


def memset(p, value, n):
    off = p * HEADER_SIZE
    memory[off:off + n] = bytes([value]) * n


def c_free(a_p):
    global free_p
    b_p = a_p - 1  # point to block header

    # Find the free block p such that b_p lies between p and its successor
    p = free_p
    while not (p < b_p < next_free[p]):
        if p >= next_free[p] and (b_p > p or b_p < next_free[p]):
            break  # freed block at start or end of arena
        p = next_free[p]

    nxt = next_free[p]
    if b_p + size[b_p] == nxt:  # join to upper neighbour
        size[b_p] += size[nxt]
        next_free[b_p] = next_free[nxt]
    else:
        next_free[b_p] = nxt

    if p + size[p] == b_p:  # join to lower neighbour
        size[p] += size[b_p]
        next_free[p] = next_free[b_p]
    else:
        next_free[p] = b_p

    free_p = p


def c_malloc(nr_of_bytes):
    """Return the unit index of the allocated memory, or None."""
    global free_p
    nr_of_units = (nr_of_bytes + HEADER_SIZE - 1) // HEADER_SIZE

    prev_p = free_p
    if prev_p is None:  # no free list yet
        next_free[BASE] = BASE
        size[BASE] = 0
        free_p = prev_p = BASE

    p = next_free[prev_p]
    while True:
        if size[p] >= nr_of_units:  # big enough
            if size[p] == nr_of_units:  # exactly
                next_free[prev_p] = next_free[p]
            else:  # allocate tail end
                size[p] -= nr_of_units
                p += size[p]
                size[p] = nr_of_units
            free_p = prev_p
            return p + 1

        if p == free_p:  # wrapped around free list
            p = c_morecore(nr_of_units)
            if p is None:
                return None  # none left

        prev_p, p = p, next_free[p]


def c_calloc(nr_of_blocks, block_size):
    p = c_malloc(nr_of_blocks * block_size)
    if p is None:
        return None
    memset(p, 0, nr_of_blocks * block_size)
    return p


def c_morecore(nr_of_units):
    """Ask the system for more memory."""
    if nr_of_units < MIN_NR_OF_UNITS:
        nr_of_units = MIN_NR_OF_UNITS

    u_p = sbrk(nr_of_units * HEADER_SIZE)
    size[u_p] = nr_of_units
    c_free(u_p + 1)
    return free_p


def main():
    test_malloc_str_p = c_malloc(27)
    if test_malloc_str_p is None:
        print("Error: malloc faild to allocate the requrested memory.")
        return 1

    strcpy(test_malloc_str_p, "Content from malloc here.")
    print(string_at(test_malloc_str_p))
    c_free(test_malloc_str_p)

    test_calloc_str_p = c_calloc(27, 1)
    if test_calloc_str_p is None:
        print("Error: calloc faild to allocate the requrested memory.")
        return 1

    strcpy(test_calloc_str_p, "Content from calloc here.")
    print(string_at(test_calloc_str_p))
    c_free(test_calloc_str_p)
    return 0


if __name__ == "__main__":
    sys.exit(main())
