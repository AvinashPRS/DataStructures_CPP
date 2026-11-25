"""
Problem:
    Given a number written in roman, check if it is valid or not
    I:1, V:5, X:10, L:50, C:100, D:500, M:1000

Input:
    roman_num: string

Output:
    bool

TC: O(n), n: no. of symbols
"""

ROMAN_MAPPINGS = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

# Smaller symbol -> larger symbols it may legally precede
VALID_EXCEPTIONS = {"I": "VX", "X": "LC", "C": "DM"}


def is_valid_roman(roman_num):
    """
    The roman number is a sequence of symbols in descending order except
    for some cases, where a smaller sym can appear immediately before a larger symbol.
    The cases are:
    1. I before V and X
    2. X before L and C
    3. C before D and M
    Also these cases cannot occur immediately one after another
    Eg: DXCIV is valid but IXC is invalid

    Note: the original C++ compared integer values against chars ('I', 'X', ...)
    so those checks never fired; here the symbols themselves are compared.
    """
    # keeps track of whether an exception case has occured recently
    exception_case = False
    n = len(roman_num)

    for i in range(n):
        cur = roman_num[i]
        # when the next sym is greater than the current sym
        if i + 1 < n and ROMAN_MAPPINGS[cur] < ROMAN_MAPPINGS[roman_num[i + 1]]:
            # check if symbols follow the valid exceptions
            if roman_num[i + 1] not in VALID_EXCEPTIONS.get(cur, ""):
                return False

            # two exception cases cannot occur one after another
            if exception_case:
                return False
            exception_case = True
        else:
            # current case is not an exception case
            exception_case = False

    return True


if __name__ == "__main__":
    print(is_valid_roman("XIV"))
    print(is_valid_roman("IXC"))
    print(is_valid_roman("DXCIV"))
