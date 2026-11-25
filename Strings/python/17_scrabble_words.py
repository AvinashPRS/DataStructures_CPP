"""Generate all words (of every length) that can be formed from the letters of a string."""


def generate_words(s, buf, visited):
    """
    s: valid input string from which words have to be generated
    buf: list holding the current word that has been generated
    visited: indicates if character in input string has already been visited
    """
    # Output all strings that we generate
    print("".join(buf))

    # Recursion termination condition
    if len(buf) >= len(s):
        return

    for i in range(len(s)):
        if not visited[i]:
            buf.append(s[i])
            visited[i] = True
            generate_words(s, buf, visited)
            visited[i] = False
            buf.pop()


def test(s):
    generate_words(s, [], [False] * len(s))
    print("______________________________\n")


if __name__ == "__main__":
    test("")
    test("A")
    test("ABCDE")

    print("Test passed")
