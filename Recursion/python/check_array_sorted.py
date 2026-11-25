"""
Recursively check whether an array is strictly increasing.
"""


def check_if_increasing(arr, idx=0):
    # Base Case: If we've reached the last element, the array is successfully sorted
    if idx >= len(arr) - 1:
        return True

    # Optimization: Check the current pair FIRST.
    # If it's not strictly increasing, fail immediately and stop recursing!
    if arr[idx] >= arr[idx + 1]:
        return False

    # Move to the next pair
    return check_if_increasing(arr, idx + 1)


if __name__ == "__main__":
    arr1 = [1, 6, 3, 4, 5]

    if check_if_increasing(arr1):
        print("Strictly Increasing")
    else:
        print("Not Strictly Increasing")  # Output: Not Strictly Increasing
