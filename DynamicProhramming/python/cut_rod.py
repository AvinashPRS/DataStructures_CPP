"""
Cutting a rod problem.

Given a rod of length n inches and a list of prices that contains prices of all
pieces of size <= n, determine the maximum profit obtainable by cutting up the
rod and selling the pieces.

Algorithm: break the rod into every smaller piece possible and compute the maximum
profit for smaller pieces, building up the solution for larger pieces bottom-up.
"""


def max_profit_by_cutting_rod(price, n):
    """
    price: list of prices, price[j-1] is the price of a piece of length j
    n: size of the rod in inches
    Return value: maximum profit obtainable for an n inch rod
    """
    profit = [0] * (n + 1)  # profit[i] holds maximum profit for i inch rod

    # outer loop selects size of rod; inner loop evaluates every possible cut on it
    for i in range(1, n + 1):
        q = float("-inf")
        for j in range(1, i + 1):
            q = max(q, price[j - 1] + profit[i - j])
        profit[i] = q
    return profit[n]


def test():
    # Test 1
    n1 = 8
    price1 = [1, 2, 4, 6, 8, 45, 21, 9]
    max_profit1 = max_profit_by_cutting_rod(price1, n1)
    assert max_profit1 == 47
    print(f"Maximum profit with {n1} inch road is {max_profit1}")

    # Test 2
    n2 = 30
    price2 = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30,
              31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
              41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
    max_profit2 = max_profit_by_cutting_rod(price2, n2)
    assert max_profit2 == 90
    print(f"Maximum profit with {n2} inch road is {max_profit2}")

    # Test 3
    n3 = 5
    price3 = [2, 9, 17, 23, 45]
    max_profit3 = max_profit_by_cutting_rod(price3, n3)
    assert max_profit3 == 45
    print(f"Maximum profit with {n3} inch road is {max_profit3}")


if __name__ == "__main__":
    test()
