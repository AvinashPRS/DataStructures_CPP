"""Sort a small list and print it."""


def main():
    nums = [3, 1, 2]
    nums.sort()
    print("".join(f"{x} " for x in nums), end="")


if __name__ == "__main__":
    main()
