"""
Problem:
    Given a valid number in roman numeral system, convert that to its int equivalent
    I:1, V:5, X:10, L:50, C:100, D:500, M:1000

Input:
    roman_num: string

Output:
    Int equivalent

TC: O(n), n: no. of symbols
"""

ROMAN_MAPPINGS = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


def roman_to_integer(roman_num):
    """
    The integer equivalent is the sum of the values of the symbols except for the
    symbols where the smaller symbol precedes the greater symbol, in that case the value is
    (value greater sym - value smaller sym)
    Eg: XIV: 10 + (5-1)

    Note: the original C++ compared the characters themselves ('V' > 'I')
    instead of their values; here the symbol values are compared.
    """
    result = 0
    i = 0
    n = len(roman_num)
    while i < n:
        cur = ROMAN_MAPPINGS[roman_num[i]]
        # see the next symbol
        if i + 1 < n and ROMAN_MAPPINGS[roman_num[i + 1]] > cur:
            result += ROMAN_MAPPINGS[roman_num[i + 1]] - cur
            # skip the next index since it has already been accounted for
            i += 2
        else:
            result += cur
            i += 1
    return result


if __name__ == "__main__":
    print(roman_to_integer("XIV"))
    print(roman_to_integer("XIVII"))
    print(roman_to_integer("VIII"))
