"""
Given two integers in array form (the sign is on the first digit), multiply them and
return the result in array form.
Input: int array, int array
Output: result array

Solution:
    Grade-school multiplication: multiply each digit of 'b' with each digit of 'a'
    from the end, accumulating into result[i + j + 1] and carrying into result[i + j].

    TC: O(nm), n: no. of digits of number 1, m: no. of digits of number 2
    SC: O(n + m)
"""


def multiply_numbers(a, b):
    is_negative = (a[0] < 0) != (b[0] < 0)
    a = [abs(a[0])] + a[1:]
    b = [abs(b[0])] + b[1:]

    result = [0] * (len(a) + len(b))
    for i in range(len(b) - 1, -1, -1):
        for j in range(len(a) - 1, -1, -1):
            result[i + j + 1] += a[j] * b[i]
            result[i + j] += result[i + j + 1] // 10
            result[i + j + 1] %= 10

    # Remove leading zeros (keep at least one digit)
    first_non_zero = next((k for k, d in enumerate(result) if d != 0), len(result) - 1)
    result = result[first_non_zero:]

    if is_negative and result[0] != 0:
        result[0] = -result[0]
    return result


def to_int(digits):
    sign = -1 if digits[0] < 0 else 1
    return sign * int("".join(str(abs(d)) for d in digits))


if __name__ == "__main__":
    b = [4, 2, 3, 7, 0, 7, 7, 2, 1, 3, 1, 2]
    a = [-2, 6, 1, 3, 3, 1, 2, 1, 7, 2, 8, 7]
    result = multiply_numbers(a, b)
    print(*result)
    assert to_int(result) == to_int(a) * to_int(b)
