"""
Given a string consisting of brackets, parenthesis, braces. Check if the brackets are balanced or not.
A bracket is balanced if there is a closing bracket for its opening bracket.
Input: string
Output: bool

Solution:
    The point to note is that for each right bracket if we see a left bracket before it which is not
    of the same type then it cannot be balanced.
    We scan from left to right. If it is a left bracket we push it to a stack.
    If it is a right bracket then check if the stack is empty or not.
    If it is empty means that there is no left bracket to match, return false.
    If it is not empty check what type of bracket is there, if different type return false

    Also if after scanning the left bracket stack is not empty, return false since there is no right bracket for it
    TC: O(n), n: no. of elements
    SC: O(n)
"""

MATCHING = {")": "(", "]": "[", "}": "{"}


def is_balanced(brackets):
    """Checks if the brackets are balanced or not."""
    # for storing the left brackets
    s = []

    # start scanning from left
    for ch in brackets:
        # if it is a left bracket push
        if ch in "([{":
            s.append(ch)
        else:  # right bracket encountered
            # if there is no left bracket to match, then unbalanced
            if not s:
                return False

            # if the left bracket is of different type
            if s[-1] != MATCHING.get(ch):
                return False

            s.pop()  # matching opening and closing brackets

    return not s


if __name__ == "__main__":
    expr = "{}(){({)}{}"
    print(is_balanced(expr))
