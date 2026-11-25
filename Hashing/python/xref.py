"""
Cross-reference table (Accelerated C++ §7.3): map each word read from stdin
to the line numbers it occurs on.

Example:
    printf "the cat\\nthe dog\\n" | python3 xref.py
"""
import sys


def split(s):
    return s.split()


def xref(stream, find_words=split):
    """Note the default word-splitter is `split`, but any function str -> list[str] can be passed."""
    ret = {}
    for line_number, line in enumerate(stream, start=1):
        for word in find_words(line):
            lines = ret.setdefault(word, [])
            # push the line number if it does not exist already
            if line_number not in lines:
                lines.append(line_number)
    return ret


if __name__ == "__main__":
    ret = xref(sys.stdin)

    # dict sorted by key, like std::map
    for word in sorted(ret):
        print(f"{word} occurs on line(s): " + ", ".join(str(n) for n in ret[word]))
