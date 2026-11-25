# Chapter 8, exercise 5 (part 2): xref writes (word, lines) pairs to a sink.
import sys

from _paths import use_chapter

use_chapter(5)
from split import split  # noqa: E402


def xref(stream, out, find_words=split):
    ret = {}
    for line_number, line in enumerate(stream.read().splitlines(), start=1):
        for word in find_words(line):
            lines = ret.setdefault(word, [])
            if line_number not in lines:
                lines.append(line_number)
    for item in sorted(ret.items()):
        out(item)


def main():
    ret = {}
    xref(sys.stdin, lambda item: ret.__setitem__(*item))

    for word in sorted(ret):
        lines = ret[word]
        print(f"{word} occurs on line{'s: ' if len(lines) > 1 else ': '}"
              + ", ".join(map(str, lines)))


if __name__ == "__main__":
    main()
