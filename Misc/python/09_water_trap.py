"""Amount of water trapped by a histogram."""
import sys


def handle_error():
    print("Error occured")
    sys.exit(1)


def water_trap(histogram):
    """
    histogram[i] contains the height of the bar at location i (n >= 1).
    Returns the amount of water that can be trapped.
    """
    n = len(histogram)
    left_max = [0] * n
    right_max = [0] * n

    # left max of bar i is the tallest bar in region [0, i]
    left_max[0] = histogram[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], histogram[i])

    # right max of bar i is the tallest bar in region [i, n-1]
    total_water = 0
    right_max[n - 1] = histogram[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], histogram[i])
        smaller_max = min(left_max[i], right_max[i])
        # water that can be stored on top of bar i
        total_water += smaller_max - histogram[i]
    return total_water


def test():
    histogram = [3, 1, 4, 0, 2, 5, 0, 3, 2]
    total_water = water_trap(histogram)
    print(f"Total water trapped = {total_water}")
    if total_water != 11:
        handle_error()


def main():
    test()
    print("Test passed ")


if __name__ == "__main__":
    main()
