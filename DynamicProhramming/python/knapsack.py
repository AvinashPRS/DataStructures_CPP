"""
Given a knapsack which has a weight limit and lists of values and weights for
objects, maximize the value of the knapsack by filling it with objects.

Solution:
    For each object:
        that object can be included (if its weight does not exceed the capacity)
        the object can be excluded
    TC: O(ns), n: no. of items and s: knapsack weight
    SC: O(ns)
"""
from dataclasses import dataclass


@dataclass
class Item:
    weight: int
    value: int


def maximum_knapsack_value(arr, n, s, cache):
    # if there are no items left
    if n <= 0:
        return 0

    if cache[n - 1][s] == -1:
        # we can either include current item or exclude it
        include_item = (arr[n - 1].value + maximum_knapsack_value(arr, n - 1, s - arr[n - 1].weight, cache)
                        if arr[n - 1].weight <= s else 0)
        exclude_item = maximum_knapsack_value(arr, n - 1, s, cache)

        cache[n - 1][s] = max(include_item, exclude_item)
    return cache[n - 1][s]


def optimum_knapsack_value(arr, s):
    """maximizes the knapsack value"""
    # each entry (i, j) is the optimum knapsack value when the
    # max weight can be 'j' and there are 'i' items
    cache = [[-1] * (s + 1) for _ in range(len(arr))]
    return maximum_knapsack_value(arr, len(arr), s, cache)


if __name__ == "__main__":
    arr = [Item(10, 60), Item(20, 100), Item(30, 120)]
    s = 50
    print(optimum_knapsack_value(arr, s))
