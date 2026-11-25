"""
Cross-reference table that writes its results to an "output iterator".

The C++ version took a template output iterator (e.g. an inserter into a map).
In Python we pass a callable `out(word, line_numbers)` that receives each entry.

Example:
    printf "the cat\\nthe dog\\n" | python3 xref_iterator.py
"""
import sys


def split(s):
    return s.split()


def xref(stream, out, find_words=split):
    ret = {}
    for line_number, line in enumerate(stream, start=1):
        for word in find_words(line):
            lines = ret.setdefault(word, [])
            if line_number not in lines:
                lines.append(line_number)

    # write results to the output "iterator", in key order
    for word in sorted(ret):
        out(word, ret[word])


if __name__ == "__main__":
    ret = {}
    xref(sys.stdin, ret.__setitem__)

    for word, lines in ret.items():
        label = "lines: " if len(lines) > 1 else "line: "
        print(f"{word} occurs on {label}" + ", ".join(str(n) for n in lines))
