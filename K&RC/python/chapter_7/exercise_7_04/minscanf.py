"""Exercise 7-4: a private version of scanf analogous to minprintf.

Python has no pointer arguments, so minscanf returns the list of converted
values instead.

run: python3 minscanf.py <<< "1 2 3 4 5r hello 2.3"
"""
import re
import sys

PATTERNS = {
    "d": (r"[+-]?\d+", lambda s: int(s, 10)),
    "i": (r"[+-]?(0[xX][0-9a-fA-F]+|0[0-7]*|[1-9]\d*)", lambda s: int(s, 0)
          if not re.fullmatch(r"[+-]?0[0-7]+", s) else int(s, 8)),
    "o": (r"[+-]?[0-7]+", lambda s: int(s, 8)),
    "u": (r"[+-]?\d+", lambda s: int(s, 10) & 0xFFFFFFFF),
    "x": (r"[+-]?(0[xX])?[0-9a-fA-F]+", lambda s: int(s, 16)),
    "s": (r"\S+", str),
    "e": (r"[+-]?(\d+\.?\d*|\.\d+)([eE][+-]?\d+)?", float),
}
PATTERNS["f"] = PATTERNS["g"] = PATTERNS["e"]


class Scanner:
    def __init__(self, text):
        self.text = text
        self.pos = 0

    def minscanf(self, fmt):
        values = []
        i = 0
        while i < len(fmt):
            if fmt[i] != "%":
                i += 1
                continue
            i += 1
            conv = fmt[i] if i < len(fmt) else ""
            i += 1

            if conv == "c":  # %c does not skip white space
                if self.pos < len(self.text):
                    values.append(self.text[self.pos])
                    self.pos += 1
                continue

            if conv not in PATTERNS:
                continue

            while self.pos < len(self.text) and self.text[self.pos].isspace():
                self.pos += 1
            regex, convert = PATTERNS[conv]
            m = re.compile(regex).match(self.text, self.pos)
            if m:
                values.append(convert(m.group(0)))
                self.pos = m.end()
        return values


def main():
    sc = Scanner(sys.stdin.read())

    (decimal,) = sc.minscanf("%d") or [0]
    (integer,) = sc.minscanf("%i") or [0]
    (octal,) = sc.minscanf("%o") or [0]
    (unsigned_decimal,) = sc.minscanf("%u") or [0]
    (hexadecimal_integer,) = sc.minscanf("%x") or [0]
    (character,) = sc.minscanf("%c") or [""]
    (string,) = sc.minscanf("%s") or [""]
    (float_point_number,) = sc.minscanf("%f") or [0.0]

    print("decimal: %d" % decimal)
    print("integer: %i" % integer)
    print("octal: %o" % octal)
    print("unsigned_decimal: %u" % unsigned_decimal)
    print("hexadecimal_integer: %x" % hexadecimal_integer)
    print("character: %s" % character)
    print("str: %s" % string)
    print("float_point_number: %f" % float_point_number)


if __name__ == "__main__":
    main()
