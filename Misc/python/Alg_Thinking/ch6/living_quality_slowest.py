"""Living Quality - sort every rectangle to find its median (slowest)."""


def median(top_row, left_col, bottom_row, right_col, q):
    cur_rectangle = sorted(q[i][j]
                           for i in range(top_row, bottom_row + 1)
                           for j in range(left_col, right_col + 1))
    return cur_rectangle[len(cur_rectangle) // 2]


def rectangle(r, c, h, w, q):
    best = r * c + 1
    for top_row in range(r - h + 1):
        for left_col in range(c - w + 1):
            bottom_row = top_row + h - 1
            right_col = left_col + w - 1
            result = median(top_row, left_col, bottom_row, right_col, q)
            if result < best:
                best = result
    return best


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
