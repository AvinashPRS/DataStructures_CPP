"""Print all permutations of a string (backtracking)."""


def generate_permutations(str1, buf, pos, visited, length):
    """
    str1: input string whose permutations have to be formed
    buf: list storing the current permutation
    pos: current position in buf
    visited: visited[i] is True if str1[i] is already used
    """
    if pos == length:
        print("".join(buf[:pos]))
        return
    for i in range(length):
        if not visited[i]:
            buf[pos] = str1[i]
            visited[i] = True
            generate_permutations(str1, buf, pos + 1, visited, length)
            visited[i] = False


def test(str1):
    length = len(str1)
    buf = [""] * (length + 1)
    visited = [False] * length
    print(f"Input: {str1}")
    generate_permutations(str1, buf, 0, visited, length)
    print("______________________________\n")


def main():
    test("")
    test("A")
    test("ABCDE")
    print("Test passed")


if __name__ == "__main__":
    main()
