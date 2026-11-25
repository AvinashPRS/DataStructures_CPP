"""
Problem:
    Find all possible mnemonics for a given input number.
    Each digit key on keypad has 3-4 chars on them, except for 1 and 0.
    Find all such cmb for a number.
    Eg. 223: abd, aad ... etc

Input:
    num: string

Output:
    list of strings
TC: T(n) = 4T(n-1)
        = O(4^n)
"""

# keypad chars for each of the digits
KEYPAD_MAPPINGS = ["0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]


def print_mnemonics(mnemonics):
    for m in mnemonics:
        print(m)
    print()


def generate_mnemonics(mnemonics, phone_num, n, curr_mnemonic):
    """Finds mnemonics for a given number"""
    # when all the digits have been processed
    if n == len(phone_num):
        mnemonics.append("".join(curr_mnemonic))
        return

    # try all the chars for the current digit
    for c in KEYPAD_MAPPINGS[int(phone_num[n])]:
        # try the current char
        curr_mnemonic.append(c)
        # recurse further
        generate_mnemonics(mnemonics, phone_num, n + 1, curr_mnemonic)
        # remove the current char to allow the next in line char
        curr_mnemonic.pop()


def find_mnemonics_driver(phone_num):
    """Driver function for finding the mnemonics for a phone number"""
    mnemonics = []
    generate_mnemonics(mnemonics, phone_num, 0, [])
    return mnemonics


if __name__ == "__main__":
    print_mnemonics(find_mnemonics_driver("123"))
