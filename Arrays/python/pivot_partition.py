"""
Given a pivot index, partition the array such that all elements smaller than the
pivot are on the left, greater are on the right and equal are in the middle.
Input: int array
Output: arranged array

Solution 1:
    Maintain these ranges:
    1. smaller than pivot: [0 : smaller - 1]
    2. equal to pivot:     [smaller : equal - 1]
    3. unclassified:       [equal : larger - 1]
    4. larger than pivot:  [larger : n - 1]
    TC: O(n)
    SC: O(1)

Solution 2:
    Two passes:
    1. forward pass: move all smaller elements to the left
    2. backward pass: move all larger elements to the right
    TC: O(n)
    SC: O(1)
"""


def partition_array_solution1(pivot_idx, arr):
    arr = list(arr)
    pivot = arr[pivot_idx]
    smaller, equal, larger = 0, 0, len(arr)

    while equal < larger:
        if arr[equal] < pivot:
            arr[equal], arr[smaller] = arr[smaller], arr[equal]
            equal += 1
            smaller += 1
        elif arr[equal] == pivot:
            equal += 1
        else:
            larger -= 1
            arr[equal], arr[larger] = arr[larger], arr[equal]
    return arr


def partition_array_solution2(pivot_idx, arr):
    arr = list(arr)
    pivot = arr[pivot_idx]

    # Forward pass
    smaller = 0
    for i in range(len(arr)):
        if arr[i] < pivot:
            arr[smaller], arr[i] = arr[i], arr[smaller]
            smaller += 1

    # Backward pass
    larger = len(arr) - 1
    j = len(arr) - 1
    while j >= 0 and arr[j] >= pivot:
        if arr[j] > pivot:
            arr[j], arr[larger] = arr[larger], arr[j]
            larger -= 1
        j -= 1
    return arr


def is_partitioned(arr, pivot):
    states = [0 if x < pivot else 1 if x == pivot else 2 for x in arr]
    return states == sorted(states)


if __name__ == "__main__":
    arr = [1, 23, 4, 67, 2, 898, 2, 9, 56, 4, 67, 23, 1, 98]
    print("Originally:")
    print(*arr, "\n")
    pivot_idx = 3

    r1 = partition_array_solution1(pivot_idx, arr)
    r2 = partition_array_solution2(pivot_idx, arr)
    print(*r1, "\n")
    print(*r2)
    assert is_partitioned(r1, arr[pivot_idx]) and is_partitioned(r2, arr[pivot_idx])
