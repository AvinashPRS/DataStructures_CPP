"""Merge k sorted arrays using a hand-written min heap."""
import random
import sys

MAX_NUM_TESTS = 10
MAX_NUM_ELEMENTS = 10
MAX_VALUE = 100
MAX_NUM_ARRAYS = 5
INF = float("inf")


def handle_error():
    print("Test failed")
    sys.exit(1)


class Node:
    __slots__ = ("value", "array_no")

    def __init__(self, value, array_no):
        self.value = value
        self.array_no = array_no


def heapify(heap, pos, heap_size):
    """
    heap - min heap of nodes
    pos - position of the heap that may need to be fixed
    heap_size - current number of nodes in the heap
    """
    left = 2 * pos + 1
    right = 2 * pos + 2
    ix_of_smallest = pos

    # Find which of the three are the smallest - heap[pos] OR left child OR right child
    if left < heap_size and heap[left].value < heap[ix_of_smallest].value:
        ix_of_smallest = left
    if right < heap_size and heap[right].value < heap[ix_of_smallest].value:
        ix_of_smallest = right

    if ix_of_smallest != pos:
        # If pos doesn't contain the smallest node, swap the smallest node into pos
        heap[pos], heap[ix_of_smallest] = heap[ix_of_smallest], heap[pos]
        heapify(heap, ix_of_smallest, heap_size)


def merge_k_sorted_arrays(arrays, n, k):
    """
    arrays: the arrays to be merged
    n: number of elements in each array
    k: number of arrays
    Returns the merged result.
    """
    result = []

    # Store the first element in each array into the heap
    heap = [Node(arrays[i][0], i) for i in range(k)]
    arr_pos = [1] * k

    # Construct the initial heap. Last non-leaf node is at (k // 2) - 1
    for i in range(k // 2 - 1, -1, -1):
        heapify(heap, i, k)

    # Process the remaining elements in the arrays
    while heap[0].value != INF:
        # Root of the heap will have the lowest value
        result.append(heap[0].value)

        array_no = heap[0].array_no
        pos = arr_pos[array_no]

        # Replace the root with the next element in that array
        heap[0].value = INF if pos >= n else arrays[array_no][pos]

        # Re-adjust the heap after replacing the root
        heapify(heap, 0, k)
        arr_pos[array_no] += 1

    return result


def print_array(array):
    print("".join(f"{x} " for x in array))


def test_01(num_arrays, num_elements):
    arrays = [sorted(random.randrange(MAX_VALUE) for _ in range(num_elements))
              for _ in range(num_arrays)]

    for i, arr in enumerate(arrays):
        print(f"Array {i}: ", end="")
        print_array(arr)

    result = merge_k_sorted_arrays(arrays, num_elements, num_arrays)

    print("Output : ", end="")
    print_array(result)

    expected_result = sorted(x for arr in arrays for x in arr)
    if result != expected_result:
        handle_error()


if __name__ == "__main__":
    for _ in range(MAX_NUM_TESTS):
        num_arrays = max(2, 1 + random.randrange(MAX_NUM_ARRAYS))
        num_elements = 1 + random.randrange(MAX_NUM_ELEMENTS)
        test_01(num_arrays, num_elements)
        print("\n_________________________________________________\n")
    print("Test passed")
