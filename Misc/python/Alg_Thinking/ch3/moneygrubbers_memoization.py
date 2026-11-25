"""Moneygrubbers - memoization solution."""
import sys

sys.setrecursionlimit(10000)

SIZE = 200


def solve_k(num, price, unit_price, num_items, memo):
    if memo[num_items] != -1:
        return memo[num_items]
    if num_items == 0:
        memo[num_items] = 0
        return 0
    best = solve_k(num, price, unit_price, num_items - 1, memo) + unit_price
    for n, p in zip(num, price):
        if num_items - n >= 0:
            result = solve_k(num, price, unit_price, num_items - n, memo)
            best = min(best, result + p)
    memo[num_items] = best
    return best


def solve(num, price, unit_price, num_items, memo):
    best = solve_k(num, price, unit_price, num_items, memo)
    for i in range(num_items + 1, SIZE):
        best = min(best, solve_k(num, price, unit_price, i, memo))
    return best


def main():
    """Input per test case:
        unit_price num_schemes
        num price           (num_schemes lines)
        k1 k2 k3 ...        (item counts to query)
    """
    lines = [ln for ln in sys.stdin.read().splitlines() if ln.strip()]
    pos = 0
    test_case = 0
    while pos < len(lines):
        head = lines[pos].split()
        pos += 1
        unit_price, num_schemes = float(head[0]), int(head[1])
        num, price = [], []
        for _ in range(num_schemes):
            a, b = lines[pos].split()
            pos += 1
            num.append(int(a))
            price.append(float(b))
        test_case += 1
        print(f"Case {test_case}:")
        memo = [-1] * SIZE
        for num_items in (int(x) for x in lines[pos].split()):
            result = solve(num, price, unit_price, num_items, memo)
            print(f"Buy {num_items} for ${result:.2f}")
        pos += 1


if __name__ == "__main__":
    main()
