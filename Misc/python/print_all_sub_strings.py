"""Print all substrings of a string."""


def print_all_sub_strings(str1):
    n = len(str1)
    # Generate all pairs (i, j) where i <= j and print str1[i..j]
    for i in range(n):
        for j in range(i, n):
            print(str1[i:j + 1])


def main():
    print_all_sub_strings("ABCDE")
    print("Test passed")


if __name__ == "__main__":
    main()
