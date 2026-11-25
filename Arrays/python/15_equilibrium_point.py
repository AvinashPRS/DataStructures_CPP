"""
Find the equilibrium point of an array: index i where the sum of elements to the
left of i equals the sum of elements to the right of i.

Solution:
    right_sum = total sum. Walk left to right, subtracting a[i] from right_sum and
    comparing with left_sum, then adding a[i] to left_sum.

    TC: O(n)
    SC: O(1)
"""


def find_equilibrium_point(a):
    """Returns the index of the equilibrium point, or -1 if none exists."""
    right_sum = sum(a)
    left_sum = 0
    for i, x in enumerate(a):
        right_sum -= x
        if left_sum == right_sum:
            return i
        left_sum += x
    return -1


if __name__ == "__main__":
    a = [-50, 100, 80, 30, -60, 10, 70]
    print("Input :", *a)
    result = find_equilibrium_point(a)
    print("Equilibrium point index =", result)
    assert result == 2, "Error occured"
    print("Test passed")
