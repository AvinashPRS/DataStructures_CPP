"""Generate all properly nested combinations of braces, brackets and parenthesis."""
import sys

OPENING = "{[("
CLOSING = "}])"
MATCHING = {"}": "{", "]": "[", ")": "("}
CLOSER_FOR = {"{": "}", "[": "]", "(": ")"}


def handle_error():
    print("Test failed")
    sys.exit(1)


def verify(str1):
    """Verify if the braces, brackets and parenthesis are properly nested"""
    s = []

    for c in str1:
        if c in OPENING:
            # If we get an opening character, push it on to the stack
            s.append(c)
        elif c in CLOSING:
            # If we get a closing character, then the character on top of
            # stack should be the corresponding opening character
            if not s:
                handle_error()
            if s[-1] != MATCHING[c]:
                handle_error()
            # Since we have matched the opening and closing character,
            # remove the opening character from the stack
            s.pop()
        else:
            # We found a character other than a brace, bracket or parenthesis
            handle_error()

    # At the end of processing, the stack should be empty
    if s:
        handle_error()


def process_string(str1):
    print(str1)
    verify(str1)


def find_unmatched(buf, pos):
    """
    Helper function for finding the nearest unmatched opening character
    buf: list containing braces, brackets and parenthesis
    pos: we will search for unmatched opening character from pos - 1 to 0
    Returns: index of the first unmatched character when traversing from
        pos - 1 to 0 if it exists, -1 otherwise
    """
    n_braces = n_brackets = n_parenthesis = 0

    # When we get a closing character, decrement the count by 1,
    # when we get an opening character, increment the count by 1
    for back_pos in range(pos - 1, -1, -1):
        c = buf[back_pos]
        if c == "{":
            n_braces += 1
        elif c == "[":
            n_brackets += 1
        elif c == "(":
            n_parenthesis += 1
        elif c == "}":
            n_braces -= 1
        elif c == "]":
            n_brackets -= 1
        elif c == ")":
            n_parenthesis -= 1

        # If we encounter more opening characters than closing characters
        # as we traverse backwards, then we have found the location of the mismatch
        if n_braces > 0 or n_brackets > 0 or n_parenthesis > 0:
            return back_pos

    return -1


def print_nesting(buf, pos, n_max, n_open, n_close):
    """
    Main function for printing the braces, brackets and parenthesis
    buf: list used to store braces, brackets and parenthesis
    pos: next free position in buf
    n_max: maximum number of opening characters (equal to max closing characters)
    n_open: number of opening characters currently in buf
    n_close: number of closing characters currently in buf
    """
    # Condition for terminating the recursion
    if n_close == n_max:
        process_string("".join(buf[:pos]))
        return

    if n_open < n_max:
        # Add an opening brace / bracket / parenthesis and recurse
        for c in OPENING:
            buf[pos] = c
            print_nesting(buf, pos + 1, n_max, n_open + 1, n_close)

    unmatched_pos = find_unmatched(buf, pos)
    if n_open > n_close and unmatched_pos >= 0:
        # To balance the characters, add the closing character corresponding
        # to nearest unmatched character and recurse
        buf[pos] = CLOSER_FOR[buf[unmatched_pos]]
        print_nesting(buf, pos + 1, n_max, n_open, n_close + 1)


def test_01():
    for i in range(1, 5):
        buf = [""] * (2 * i)
        print_nesting(buf, 0, i, 0, 0)
        print("\n______________________________________")


if __name__ == "__main__":
    test_01()

    print("Test passed")
