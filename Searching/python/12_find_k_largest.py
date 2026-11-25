"""Find the k largest elements of an array using a min-heap of size k."""
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
    """
    Helper function to perform heapify
    heap: min heap. Maximum number of elements in heap is k
    pos: position of the heap that may need to be fixed
    heap_size: current number of nodes in the heap
    """
    left = 2 * pos
    right = 2 * pos + 1
    ix_of_smallest = pos

    # Find which of the three are the smallest: heap[pos] OR left child
    # OR right child
    if left < heap_size and heap[pos] > heap[left]:
        ix_of_smallest = left
    if right < heap_size and heap[ix_of_smallest] > heap[right]:
        ix_of_smallest = right

    if ix_of_smallest != pos:
        # If pos doesn't contain the smallest value,
        # then swap the smallest value into pos
        heap[pos], heap[ix_of_smallest] = heap[ix_of_smallest], heap[pos]

        # Recursively re-adjust the heap
        heapify(heap, ix_of_smallest, heap_size)


def find_k_largest(a, k):
    """
    Main function to find the k largest elements
    a: list in which we have to find the k largest elements. len(a) > 0
    k: the number of largest elements that we need to find. k <= len(a)
    Returns: heap containing the k largest elements
    """
    # Store the first k elements of the array in the heap
    heap = a[:k]

    # Construct the initial min-heap
    for i in range(k - 1, -1, -1):
        heapify(heap, i, k)

    for i in range(k, len(a)):
        # The root of the heap will have the smallest item in the heap.
        # If current item in array is greater than root of the heap, then
        # place current item into root of the heap and readjust the heap
        if a[i] > heap[0]:
            heap[0] = a[i]
            heapify(heap, 0, k)

    return heap


def print_array(a):
    print("".join(f"{x} " for x in a))


def test_01():
    # Randomly generate the k value
    k = 1 + random.randrange(MAX_K_VALUE)

    print(f"K = {k}")

    # Randomly generate the numbers in the array
    a = [random.randrange(MAX_VALUE) for _ in range(MAX_NUM_ELEMS)]

    print("Input  : ", end="")
    print_array(a)

    # Find the k largest elements using the heap
    heap = find_k_largest(a, k)

    # Sort the array in descending order
    a.sort(reverse=True)

    # Print the top k elements in the heap. Note that elements in the heap
    # will themselves NOT be in sorted order
    print("Output : ", end="")
    print_array(heap)

    # Verify that each element in the heap is present in the top k elements
    # in the sorted array
    top_k = a[:k]
    for x in heap:
        if x not in top_k:
            handle_error()


if __name__ == "__main__":
    for _ in range(MAX_NUM_TESTS):
        test_01()
        print("\n_________________________________________________\n")
    print("Test passed")
