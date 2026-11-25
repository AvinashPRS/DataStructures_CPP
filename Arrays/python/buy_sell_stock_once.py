"""
Buy and sell stock once:
    Given an array of stock prices, find the max gain that can be made by buying
    a stock once and selling it later.

Solution:
    For each price, the best gain when selling at that price is obtained by buying
    at the minimum price seen so far. Track the maximum of these gains.

    TC: O(n)
    SC: O(1)
"""


def maximize_buy_once_stock_profit(prices):
    max_profit = 0
    min_till_this = float("inf")
    for price in prices:
        min_till_this = min(min_till_this, price)
        max_profit = max(max_profit, price - min_till_this)
    return max_profit


if __name__ == "__main__":
    prices = [311, 315, 275, 295, 2320, 271, 290, 240, 255, 210]
    print(maximize_buy_once_stock_profit(prices))
