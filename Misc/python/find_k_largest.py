"""Find the k largest elements of an array using a min-heap of size k.

Note: the C version computes children as 2*pos and 2*pos+1 on a 0-indexed
heap; here the correct 0-indexed children 2*pos+1 and 2*pos+2 are used.
"""
import random
import sys

MAX_NUM_TESTS = 10
MAX_NUM_ELEMS = 20
MAX_K_VALUE = 10
MAX_VALUE = 100


def handle_error():
    print("Test failed")
    sys.exit(1)


def heapify(heap, pos, heap_size):
    """Fix the min-heap property at pos (0-indexed)."""
    left = 2 * pos + 1
    right = 2 * pos + 2
    ix_of_smallest = pos
    if left < heap_size and heap[pos] > heap[left]:
        ix_of_smallest = left
    if right < heap_size and heap[ix_of_smallest] > heap[right]:
        ix_of_smallest = right
    if ix_of_smallest != pos:
        heap[pos], heap[ix_of_smallest] = heap[ix_of_smallest], heap[pos]
        heapify(heap, ix_of_smallest, heap_size)


def find_k_largest(a, k):
    """Returns a min-heap (list) holding the k largest elements of a."""
    heap = a[:k]
    for i in range(k - 1, -1, -1):
        heapify(heap, i, k)
    for x in a[k:]:
        # root holds the smallest of the current k largest
        if x > heap[0]:
            heap[0] = x
            heapify(heap, 0, k)
    return heap


def print_array(a):
    print("".join(f"{x} " for x in a))


def test_01():
    k = 1 + random.randrange(MAX_K_VALUE)
    print(f"K = {k}")
    a = [random.randrange(MAX_VALUE) for _ in range(MAX_NUM_ELEMS)]
    print("Input  : ", end="")
    print_array(a)

    heap = find_k_largest(a, k)
    a.sort(reverse=True)

    # Elements in the heap are NOT in sorted order
    print("Output : ", end="")
    print_array(heap)

    # Each heap element must be among the top k of the sorted array
    for h in heap:
        if h not in a[:k]:
            handle_error()


def main():
    for _ in range(MAX_NUM_TESTS):
        test_01()
        print("\n_________________________________________________\n")
    print("Test passed")


if __name__ == "__main__":
    main()
