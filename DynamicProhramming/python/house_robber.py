"""
House Robber problem.

There is a row of houses. Each house has some cash, given as a non-negative integer
list money, where money[i] is the amount in the i-th house. You cannot steal from
two adjacent houses. Calculate the maximum amount of cash you can steal.

O(n) time, O(1) space.
"""


def house_robber(money):
    """
    money: list containing money in the ith house
    Return value: maximum amount of money that can be robbed
    """
    n = len(money)
    if n == 0:  # if there is no house
        return 0
    if n == 1:  # if there is only one house
        return money[0]
    if n == 2:  # if there are two houses, the one with more money is robbed
        return max(money[0], money[1])

    max_value = 0  # contains maximum stolen value at the end
    value1 = money[0]
    value2 = max(money[0], money[1])
    for i in range(2, n):
        max_value = max(money[i] + value1, value2)
        value1 = value2
        value2 = max_value

    return max_value


def test():
    print("Test 1... ", end="")
    assert house_robber([1, 2, 3, 1]) == 4  # first and third houses
    print("passed")

    print("Test 2... ", end="")
    assert house_robber([6, 7, 1, 3, 8, 2, 4]) == 19  # first, third, fifth and seventh
    print("passed")

    print("Test 3... ", end="")
    assert house_robber([]) == 0  # no house, no money
    print("passed")

    print("Test 4... ", end="")
    assert house_robber([2, 7, 9, 3, 1]) == 12  # first, third and fifth
    print("passed")


if __name__ == "__main__":
    test()
