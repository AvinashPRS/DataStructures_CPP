"""
Buy and sell stock twice:
    Given an array of stock prices, find the max gain that can be made by buying and
    selling a stock at most twice. The second stock can be bought only after the
    first is sold.

Solution:
    For each price 'i' track:
    1. max gain if the first stock is sold at price i or before (forward pass)
    2. max gain if the second stock is bought at price i and sold later
       (backward pass, using the max price after i)
    The answer is the max over i of (1) + (2).

    TC: O(n)
    SC: O(n), for saving the gains of the forward pass
"""


def maximize_buy_twice_stock_profit(prices):
    n = len(prices)
    if n == 0:
        return 0

    # gain_if_stock_sold[i]: max gain from one transaction ending at or before i
    gain_if_stock_sold = [0] * n
    max_profit = 0
    min_till_this = float("inf")
    for i, price in enumerate(prices):
        min_till_this = min(min_till_this, price)
        max_profit = max(max_profit, price - min_till_this)
        gain_if_stock_sold[i] = max_profit

    # Backward pass: buy second stock at i and sell at max price after i
    max_profit = 0
    max_after_this = float("-inf")
    for i in range(n - 1, -1, -1):
        max_after_this = max(max_after_this, prices[i])
        curr_gain = max_after_this - prices[i]
        max_profit = max(max_profit, curr_gain + gain_if_stock_sold[i])

    return max_profit


if __name__ == "__main__":
    prices = [12, 11, 13, 9, 12, 8, 14, 13, 15]
    print(maximize_buy_twice_stock_profit(prices))
