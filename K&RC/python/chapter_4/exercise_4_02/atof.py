"""Exercise 4-2: extend atof to handle scientific notation (123.45e-6)."""
import sys


def atof(s):
    n = len(s)

    def at(k):
        return s[k] if k < n else "\0"

    i = 0
    while at(i).isspace():
        i += 1

    sign = -1 if at(i) == "-" else 1
    if at(i) in "+-" and at(i) != "\0":
        i += 1

    val = 0.0
    while at(i).isdigit():
        val = 10.0 * val + (ord(s[i]) - ord("0"))
        i += 1

    if at(i) == ".":
        i += 1

    power = 1.0
    while at(i).isdigit():
        val = 10.0 * val + (ord(s[i]) - ord("0"))
        power *= 10
        i += 1

    exp_sign = 1
    exp_pwr = 0
    if at(i) in ("e", "E"):
        i += 1
        if at(i) == "-":
            exp_sign = -1
            i += 1
        elif at(i) == "+":
            i += 1

    while at(i).isdigit():
        exp_pwr = 10 * exp_pwr + (ord(s[i]) - ord("0"))
        i += 1

    while exp_pwr:
        if exp_sign == -1:
            power *= 10
        else:
            power /= 10
        exp_pwr -= 1

    return sign * val / power


def main():
    line = sys.stdin.readline()
    sys.stdout.write(line)
    print("%f" % atof(line), end="")


if __name__ == "__main__":
    main()
