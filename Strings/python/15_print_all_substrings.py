"""Print all substrings of a string."""


def print_all_sub_strings(str1):
    """str1: string whose substrings should be printed"""
    n = len(str1)

    # Generate all pairs (i, j) where i <= j
    for i in range(n):
        for j in range(i, n):
            # print the substring str1[i] to str1[j]
            print(str1[i:j + 1])


if __name__ == "__main__":
    print_all_sub_strings("ABCDE")

    print("Test passed")
