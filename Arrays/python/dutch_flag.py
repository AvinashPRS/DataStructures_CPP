"""
Dutch Flag problem:
    Given an array consisting of three colours, arrange the elements such that the
    elements with the same colour come together (partitioned around a pivot).
Input: list of colours
Output: arranged list

Solution:
    Maintain these ranges:
    1. smaller than pivot: [0 : smaller - 1]
    2. equal to pivot:     [smaller : equal - 1]
    3. unclassified:       [equal : larger - 1]
    4. larger than pivot:  [larger : n - 1]
    Traverse with 'equal'. A smaller element is swapped to 'smaller' (both advance,
    since the element swapped back is already known to equal the pivot). A larger
    element is swapped to --larger ('equal' stays, the incoming element is unclassified).

    TC: O(n)
    SC: O(1)
"""
from enum import IntEnum


class Colors(IntEnum):
    RED = 0
    WHITE = 1
    BLUE = 2


def partition_dutch_flag_colors(pivot_idx, arr):
    arr = list(arr)
    pivot = arr[pivot_idx]
    smaller, equal, larger = 0, 0, len(arr)

    while equal < larger:
        if arr[equal] < pivot:
            arr[smaller], arr[equal] = arr[equal], arr[smaller]
            smaller += 1
            equal += 1
        elif arr[equal] == pivot:
            equal += 1
        else:
            larger -= 1
            arr[equal], arr[larger] = arr[larger], arr[equal]

    return arr


if __name__ == "__main__":
    R, W, B = Colors.RED, Colors.WHITE, Colors.BLUE
    arr = [R, W, R, B, W, R, W, W, B, B, R]
    print("Originally:")
    print(*map(int, arr), "\n")
    result = partition_dutch_flag_colors(1, arr)
    print(*map(int, result))
    assert result == sorted(arr)
