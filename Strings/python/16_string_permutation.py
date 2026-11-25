"""Print all permutations of a string."""


def generate_permutations(str1, buf, pos, visited):
    """
    str1: valid input string whose permutations have to be formed
    buf: list for storing the current permutation
    pos: current position in the buf list
    visited: indicates if character in input string has already been visited
    """
    length = len(str1)

    # Recursion termination condition
    if pos == length:
        print("".join(buf))
        return

    for i in range(length):
        if not visited[i]:
            buf[pos] = str1[i]
            visited[i] = True
            generate_permutations(str1, buf, pos + 1, visited)
            visited[i] = False  # backtrack to explore other permutations


def test(str1):
    print(f"Input: {str1}")

    if len(str1) == 0:
        print()
        print("______________________________\n")
        return

    buf = [""] * len(str1)
    visited = [False] * len(str1)

    generate_permutations(str1, buf, 0, visited)

    print("______________________________\n")


if __name__ == "__main__":
    test("")
    test("A")
    test("ABCDE")

    print("Test passed")
