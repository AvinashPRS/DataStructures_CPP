"""Merge K sorted arrays using divide and conquer (pairwise merging). TC: O(N log K)"""
import random
import sys


def merge_two_arrays(arr1, arr2):
    """Merges two sorted arrays. TC: O(len1 + len2)"""
    merged = []
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1

    # Append any remaining elements
    merged.extend(arr1[i:])
    merged.extend(arr2[j:])
    return merged


def merge_k_sorted_arrays(arrays):
    if not arrays:
        return []

    # Repeat until only 1 array is left
    while len(arrays) > 1:
        next_round_arrays = []
        # Merge arrays in pairs: (0,1), (2,3), ...
        for i in range(0, len(arrays), 2):
            if i + 1 < len(arrays):
                next_round_arrays.append(merge_two_arrays(arrays[i], arrays[i + 1]))
            else:
                # Odd array left out: pass it to the next round
                next_round_arrays.append(arrays[i])
        arrays = next_round_arrays

    return arrays[0]


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
        num_arrays = random.randint(2, 5)
        num_elements = random.randint(1, 10)
        test_01(num_arrays, num_elements)
        print("\n_________________________________________________\n")
