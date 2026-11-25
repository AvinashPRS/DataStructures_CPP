"""
Quicksort with a random pivot.
See https://en.wikipedia.org/wiki/Quicksort
YouTube lesson (C version): https://www.youtube.com/watch?v=0jDiBM68NGU
"""
import random


def quicksort(array):
    """Sort the whole list in place."""
    quicksort_recursion(array, 0, len(array) - 1)


def quicksort_recursion(array, low, high):
    if low < high:
        pivot_index = partition(array, low, high)
        quicksort_recursion(array, low, pivot_index - 1)
        quicksort_recursion(array, pivot_index + 1, high)


def partition(array, low, high):
    """Partition array[low..high] around a random pivot; return its index."""
    # random pivot avoids worst-case behaviour on unlucky inputs
    pivot_index = low + random.randrange(high - low)
    # move the pivot to the end
    if pivot_index != high:
        array[pivot_index], array[high] = array[high], array[pivot_index]
    pivot_value = array[high]

    # i marks where the elements greater than the pivot begin
    i = low
    for j in range(low, high):
        if array[j] <= pivot_value:
            array[i], array[j] = array[j], array[i]
            i += 1
    # put the pivot in its final place
    array[i], array[high] = array[high], array[i]
    return i


def main():
    a = [10, 11, 23, 44, 8, 15, 3, 9, 12, 45, 56, 45, 45]
    quicksort(a)
    print("".join(f"{x} " for x in a))


if __name__ == "__main__":
    main()
