"""Maximum loot a thief can steal without robbing adjacent houses."""
import sys


def handle_error():
    print("Error occured ")
    sys.exit(1)


def find_max_loot(house_value):
    """
    house_value: value that the thief can steal from each house
    Return value: maximum loot value that the thief can steal from all the houses
    """
    n = len(house_value)
    if n == 0:
        return 0
    if n == 1:
        return house_value[0]
    if n == 2:
        return max(house_value[0], house_value[1])

    # val1 has the max loot till the previous house,
    # val2 has the max loot till the second previous house
    val1 = max(house_value[0], house_value[1])
    val2 = house_value[0]
    cur_val = val1

    for i in range(2, n):
        # cur_val stores the maximum loot till the current house (ith house)
        cur_val = max(val2 + house_value[i], val1)
        val2, val1 = val1, cur_val

    return cur_val


def print_array(a):
    print(" ".join(str(x) for x in a) + " ")


def run_test(house_value, expected):
    print("House values : ", end="")
    print_array(house_value)

    max_loot = find_max_loot(house_value)
    print(f"Max loot = {max_loot}")

    if max_loot != expected:
        handle_error()

    print("__________________________________")


if __name__ == "__main__":
    run_test([6, 1, 2, 7], 13)
    run_test([6], 6)
    run_test([6, 4], 6)
    run_test([6, 8], 8)
    run_test([1, 6, 2, 8, 3], 14)
    print("Test passed ")
