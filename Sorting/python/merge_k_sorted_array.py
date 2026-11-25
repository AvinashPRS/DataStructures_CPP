"""Merge K sorted arrays using a min heap (heapq). TC: O(N * K * log K), SC: O(K)"""
import heapq
import random
import sys


def merge_k_sorted_arrays(arrays):
    result = []

    # Heap entries are (value, array_no, element_idx) -- this is the important
    # part: we track which array the value came from and where in it we are.
    min_heap = []

    # 1. Push the first element of each non-empty array
    for i, arr in enumerate(arrays):
        if arr:
            min_heap.append((arr[0], i, 0))
    heapq.heapify(min_heap)

    # 2. Process elements until the heap is empty
    while min_heap:
        value, array_no, element_idx = heapq.heappop(min_heap)
        result.append(value)

        # If the source array has more elements, push its next element
        next_idx = element_idx + 1
        if next_idx < len(arrays[array_no]):
            heapq.heappush(min_heap, (arrays[array_no][next_idx], array_no, next_idx))

    return result


def print_array(arr):
    print("".join(f"{x} " for x in arr))


def test_01(num_arrays, num_elements):
    arrays = [sorted(random.randint(0, 99) for _ in range(num_elements))
              for _ in range(num_arrays)]
    for i, arr in enumerate(arrays):
        print(f"Array {i}: ", end="")
        print_array(arr)

    result = merge_k_sorted_arrays(arrays)

    print("Output  : ", end="")
    print_array(result)

    expected_result = sorted(x for arr in arrays for x in arr)
    if result == expected_result:
        print("Test passed")
    else:
        print("Test failed")
        sys.exit(1)


if __name__ == "__main__":
    for _ in range(5):
        num_arrays = random.randint(2, 5)      # 2 to 5 arrays
        num_elements = random.randint(1, 10)   # 1 to 10 elements per array
        test_01(num_arrays, num_elements)
        print("\n_________________________________________________\n")
