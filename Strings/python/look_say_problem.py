"""
Problem:
    Look and Say problem: We need to find the nth term in look and say series.
    The series starts with 1 and each next term is formed by looking at the previous:
    no of digits + digit ...
    Eg: 1, one 1, two 1, one 2 one 1
        1, 11, 21, 1211, 111221, 312211

Input:
    n: int

Output:
    nth string term

TC:
    T(n) <= 2*T(n-1),
            ~ 2^n
    Each ith term can have at max twice the number of chars that (i-1)th term
    had. Also for finding nth term, we need to find the terms from 1...n.
    Total: O(n * 2^n)

Note: the original .cpp file only contained a word-count program (a copy of
word_count.cpp) despite this header; this file implements the look-and-say
series described above.
"""
import sys


def handle_error():
    print("Test failed", file=sys.stderr)
    sys.exit(1)


def next_term(s):
    """Reads the term s aloud: count of each run of same digits followed by the digit"""
    result = []
    i = 0
    while i < len(s):
        count = 1
        while i + 1 < len(s) and s[i] == s[i + 1]:
            i += 1
            count += 1
        result.append(f"{count}{s[i]}")
        i += 1
    return "".join(result)


def look_and_say(n):
    """Returns the nth (1-based) term of the look and say series"""
    s = "1"
    for _ in range(1, n):
        s = next_term(s)
    return s


def test(n, expected_result):
    result = look_and_say(n)

    if result != expected_result:
        handle_error()

    print(f"Term {n} = {result}")


if __name__ == "__main__":
    test(1, "1")
    test(2, "11")
    test(3, "21")
    test(4, "1211")
    test(5, "111221")
    test(6, "312211")

    print("Test passed")
