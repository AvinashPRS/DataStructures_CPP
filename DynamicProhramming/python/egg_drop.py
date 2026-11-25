"""Get minimum number of trials needed in worst case with n eggs and k floors."""
import sys


def egg_drop(n, k):
    egg_floor = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        if k >= 1:
            egg_floor[i][1] = 1  # n eggs..1 Floor
        egg_floor[i][0] = 0      # n eggs..0 Floor

    # Only one egg available
    for j in range(1, k + 1):
        egg_floor[1][j] = j

    for i in range(2, n + 1):
        for j in range(2, k + 1):
            egg_floor[i][j] = sys.maxsize
            for x in range(1, j + 1):
                # 1 + max(eggBreak[one less egg, lower floors],
                #         eggDoesntBreak[same # of eggs, upper floors])
                result = 1 + max(egg_floor[i - 1][x - 1], egg_floor[i][j - x])
                if result < egg_floor[i][j]:
                    egg_floor[i][j] = result

    return egg_floor[n][k]


if __name__ == "__main__":
    n, k = map(int, input("Enter number of eggs and floors: ").split())
    print(f"Minimum number of trials in worst case: {egg_drop(n, k)}")
