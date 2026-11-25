"""
Problem:
    Given a spreadsheet column id, convert that to its integer equivalent.
    A = 1, B = 2,..... Z = 26, AA = 27, AB = 28 ....

Input:
    col_id: string

Output:
    Int

TC: O(n), n=no. of chars
"""


def to_spreadsheet_int_equivalent(col_id):
    """
    We can treat it as base conversion problem, where the base is 26 and we just find the
    decimal equivalent of the column id with base 26
    """
    int_equiv = 0
    for c in col_id:
        int_equiv = int_equiv * 26 + (ord(c) - ord("A") + 1)
    return int_equiv


if __name__ == "__main__":
    print(to_spreadsheet_int_equivalent("Z"))
    print(to_spreadsheet_int_equivalent("AC"))
