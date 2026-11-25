"""Exercise 2-3: htoi converts a string of hex digits (optional 0x/0X prefix)
into its integer value."""
import sys

HEX_DIGITS = "0123456789abcdef"


def htoi(hexstr):
    s = hexstr
    if len(s) >= 2 and s[0] == "0" and s[1] in "xX":
        s = s[2:]

    result = 0
    for ch in s:
        digit = HEX_DIGITS.find(ch.lower())
        if digit < 0:
            print("Error: Not a valid hex value.\n Try this format: 0xHHHH, "
                  "where H is a hex digit.")
            continue
        result = result * 16 + digit

    return result


def main():
    line = sys.stdin.readline().rstrip("\n")
    print(htoi(line), end="")


if __name__ == "__main__":
    main()

# NOTE: The conversion algorithm from hex to dec is very similar with the
# conversion algorithm from bin to dec, but the base is not 2 but 16.
# The general formula is: x1*B^N + x2*B^(N - 1) + ... + xn*B^(N - N), where B
# is the base from we convert to dec, in this case B = 16.
