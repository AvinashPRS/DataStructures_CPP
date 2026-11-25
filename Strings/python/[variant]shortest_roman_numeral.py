"""
Problem:
    For a given integer, write the smallest roman numeral for it
    I:1, V:5, X:10, L:50, C:100, D:500, M:1000

Input:
    num: int

Output:
    shortest roman num: string

TC: O(n), n: int num
"""

# Int to roman symbols mappings
# Possible Roman symbols:
#   I:1, V:5, X:10, L:50, C:100, D:500, M:1000
#   1. I before V and X: IV:4 and IX:9
#   2. X before L and C: XL:40 and XC:90
#   3. C before D and M: CD:400 and CM:900
ROMAN_MAPPINGS = {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X",
                  40: "XL", 50: "L", 90: "XC",
                  100: "C", 400: "CD", 500: "D",
                  900: "CM", 1000: "M"}

ROMAN_VALS = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]


def shortest_roman_from_int(num):
    """
    We divide the number by the largest roman value that is smaller than
    (or equal to) the number.
    """
    if num == 0:
        return ""

    # start with the largest value
    for val in reversed(ROMAN_VALS):
        if val <= num:
            # print the sym the no. of times it can divide
            return ROMAN_MAPPINGS[val] * (num // val) + shortest_roman_from_int(num % val)

    return ""


if __name__ == "__main__":
    print(shortest_roman_from_int(10))
    print(shortest_roman_from_int(59))
    print(shortest_roman_from_int(900))
    print(shortest_roman_from_int(1300))
