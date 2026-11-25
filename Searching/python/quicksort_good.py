"""Quicksort using median-of-three pivot selection and Hoare's partition scheme."""


def median_of_three(arr, low, high):
    """
    Choose the median of low, middle, and high elements as the pivot.
    This prevents O(N^2) degradation on sorted or nearly sorted data.
    """
    mid = low + (high - low) // 2

    if arr[low] > arr[mid]:
        arr[low], arr[mid] = arr[mid], arr[low]
    if arr[low] > arr[high]:
        arr[low], arr[high] = arr[high], arr[low]
    if arr[mid] > arr[high]:
        arr[mid], arr[high] = arr[high], arr[mid]

    # Hide the chosen pivot at the 'low' index temporarily for partitioning
    arr[low], arr[mid] = arr[mid], arr[low]
    return arr[low]


def partition(arr, low, high):
    """
    Hoare's Partition Scheme.
    More efficient than Lomuto's because it performs roughly three times fewer
    swaps on average.
    """
    pivot = median_of_three(arr, low, high)
    i = low - 1
    j = high + 1

    while True:
        # Move the left index right until an element >= pivot is found
        i += 1
        while arr[i] < pivot:
            i += 1

        # Move the right index left until an element <= pivot is found
        j -= 1
        while arr[j] > pivot:
            j -= 1

        # If indices cross, the partition process is complete
        if i >= j:
            return j

        arr[i], arr[j] = arr[j], arr[i]


def quicksort_helper(arr, low, high):
    """Internal recursive quicksort function."""
    if low < high:
        # p is the partitioning index; elements at or left of p are <= elements right of p
        p = partition(arr, low, high)

        # Recursively sort elements on both sides of the partition boundary
        quicksort_helper(arr, low, p)
        quicksort_helper(arr, p + 1, high)


def quicksort(arr):
    """Clean, user-facing driver interface function."""
    if len(arr) <= 1:
        return
    quicksort_helper(arr, 0, len(arr) - 1)


if __name__ == "__main__":
    data = [24, -5, 3, 0, 100, 24, 9, -12, 55, 3]

    print("Original array: " + " ".join(map(str, data)) + " ")

    quicksort(data)

    print("Sorted array:   " + " ".join(map(str, data)) + " ")

    # Verify correct sorting orientation
    if all(data[i] <= data[i + 1] for i in range(len(data) - 1)):
        print("Verification: Array successfully sorted!")
    else:
        print("Verification: Sorting failed.")
