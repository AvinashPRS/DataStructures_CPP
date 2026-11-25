"""Living Quality - binary search, summing each rectangle directly (slow)."""


def can_make_quality(quality, r, c, h, w, q):
    zero_one = [[-1 if q[i][j] <= quality else 1 for j in range(c)]
                for i in range(r)]
    for top_row in range(r - h + 1):
        for left_col in range(c - w + 1):
            bottom_row = top_row + h - 1
            right_col = left_col + w - 1
            total = 0
            for i in range(top_row, bottom_row + 1):
                for j in range(left_col, right_col + 1):
                    total += zero_one[i][j]
            if total <= 0:
                return True
    return False


def rectangle(r, c, h, w, q):
    low, high = 0, r * c + 1
    while high - low > 1:
        mid = (low + high) // 2
        if can_make_quality(mid, r, c, h, w, q):
            high = mid
        else:
            low = mid
    return high


def main():
    # Sample from IOI 2010 "Quality of Living"
    q = [[5, 11, 12, 16, 25],
         [17, 18, 2, 7, 10],
         [4, 23, 20, 3, 1],
         [24, 21, 19, 14, 9],
         [6, 22, 8, 13, 15]]
    print(rectangle(5, 5, 3, 3, q))  # expected 9


if __name__ == "__main__":
    main()
