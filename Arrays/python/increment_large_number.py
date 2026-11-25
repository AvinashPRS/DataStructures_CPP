"""
Given a non-negative number represented as an array of digits, add 1 to the number.
Input: int array
Output: int array

Solution:
    Add 1 to the last digit and propagate the carry to the left.

    TC: O(n)
    SC: O(n)
"""


def increment_number(arr):
    result = list(arr)
    carry = 1
    for i in range(len(result) - 1, -1, -1):
        result[i] += carry
        carry = result[i] // 10
        result[i] %= 10
        if not carry:
            break

    if carry:
        result.insert(0, carry)
    return result


if __name__ == "__main__":
    arr = [9, 9, 9, 9, 9, 9, 9]
    print(*increment_number(arr))
