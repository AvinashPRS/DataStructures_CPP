"""
Print keypad combination
( 0 -> .
  1 -> abc
  2 -> def
  3 -> ghi
  4 -> jkl
  5 -> mno
  6 -> pqrs
  7 -> tu
  8 -> vwx
  9 -> yz
)
"""

KEYPAD = [".", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tu", "vwx", "yz"]


def print_keypad_combination(number, idx=0, res=""):
    """Print all the combinations."""
    if idx == len(number):
        print(res)
        return
    for curr in KEYPAD[int(number[idx])]:
        print_keypad_combination(number, idx + 1, res + curr)


if __name__ == "__main__":
    number = "2253"
    print_keypad_combination(number)
