"""Supermarket Promotion - too slow (uses linear search)."""
import sys

MAX_COST = 1000000


def extract_max(receipts):
    max_cost, max_index = -1, -1
    for i, (cost, used) in enumerate(receipts):
        if not used and cost > max_cost:
            max_index, max_cost = i, cost
    receipts[max_index][1] = True
    return max_cost


def extract_min(receipts):
    min_cost, min_index = MAX_COST + 1, -1
    for i, (cost, used) in enumerate(receipts):
        if not used and cost < min_cost:
            min_index, min_cost = i, cost
    receipts[min_index][1] = True
    return min_cost


def main():
    data = [int(x) for x in sys.stdin.read().split()]
    num_days = data[0]
    pos = 1
    receipts = []  # [cost, used]
    total_prizes = 0
    for _ in range(num_days):
        receipts_today = data[pos]
        pos += 1
        for cost in data[pos:pos + receipts_today]:
            receipts.append([cost, False])
        pos += receipts_today
        max_cost = extract_max(receipts)
        min_cost = extract_min(receipts)
        total_prizes += max_cost - min_cost
    print(total_prizes)


if __name__ == "__main__":
    main()
