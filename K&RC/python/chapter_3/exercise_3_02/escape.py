"""Exercise 3-2: escape(s, t) converts characters like newline and tab into
visible escape sequences; unescape does the reverse."""
import sys

ESCAPES = {
    "\a": "a", "\b": "b", "\f": "f", "\n": "n", "\r": "r", "\t": "t",
    "\v": "v", "\\": "\\", "?": "?", "'": "'", '"': '"',
}
UNESCAPES = {v: k for k, v in ESCAPES.items()}


def escape(src):
    out = []
    for c in src:
        if c in ESCAPES:
            out.append("\\" + ESCAPES[c])
        else:
            out.append(c)
    return "".join(out)


def unescape(src):
    out = []
    i = 0
    while i < len(src):
        c = src[i]
        if c == "\\" and i + 1 < len(src):
            i += 1
            nxt = src[i]
            if nxt in UNESCAPES:
                out.append(UNESCAPES[nxt])
            else:
                out.append("\\" + nxt)
        else:
            out.append(c)
        i += 1
    return "".join(out)


def main():
    src = sys.stdin.readline()
    sys.stdout.write(src)

    print(escape(src))

    sys.stdout.write(unescape(src))


if __name__ == "__main__":
    main()
