# Cross-reference table (§7.3/126), shared by exercises 3, 4, 7 and 8.
import sys

from _paths import use_chapter

use_chapter(5)
from split import split  # noqa: E402


def xref(stream=sys.stdin, find_words=split):
    """Map each word to the (unique) line numbers it occurs on."""
    ret = {}
    for line_number, line in enumerate(stream.read().splitlines(), start=1):
        for word in find_words(line):
            lines = ret.setdefault(word, [])
            if line_number not in lines:
                lines.append(line_number)
    return ret


def write_xref(ret, plural_aware=False, wrap=None):
    for word in sorted(ret):
        lines = ret[word]
        if plural_aware:
            out = [f"{word} occurs on line{'s: ' if len(lines) > 1 else ': '}"]
        else:
            out = [f"{word} occurs on line(s): "]
        out.append(str(lines[0]))
        for idx in range(1, len(lines)):
            out.append(", ")
            # break up the output line after every `wrap` numbers
            if wrap and idx % wrap == 0:
                out.append("\n")
            out.append(str(lines[idx]))
        print("".join(out))
