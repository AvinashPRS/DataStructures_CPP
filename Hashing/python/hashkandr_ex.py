"""
K&R Exercise 6-6: a mini #define macro preprocessor built on the K&R hash table.

Reads text from stdin. Lines of the form
    #define NAME replacement text
install NAME into the table; any later identifier matching a NAME is replaced
by its definition. Everything else is passed through unchanged.

Example:
    printf "#define MAX 100\\n#define GREETING Hello_World\\nMAX points to GREETING\\n" | python3 hashkandr_ex.py
"""
import sys

HASHSIZE = 101
MAXWORD = 100


class NList:
    def __init__(self, name, defn, next_node=None):
        self.next = next_node
        self.name = name
        self.defn = defn


hashtab = [None] * HASHSIZE


# --- Core K&R hash table ---

def hash_str(s):
    hashval = 0
    for ch in s:
        hashval = (ord(ch) + 31 * hashval) & 0xFFFFFFFF
    return hashval % HASHSIZE


def lookup(s):
    np = hashtab[hash_str(s)]
    while np is not None:
        if np.name == s:
            return np
        np = np.next
    return None


def install(name, defn):
    np = lookup(name)
    if np is None:
        hashval = hash_str(name)
        np = NList(name, defn, hashtab[hashval])
        hashtab[hashval] = np
    else:
        np.defn = defn
    return np


def free_table():
    for i in range(HASHSIZE):
        hashtab[i] = None


# --- Input parsing (character stream with one char of push-back) ---

class CharReader:
    def __init__(self, text):
        self.text = text
        self.pos = 0

    def getchar(self):
        if self.pos >= len(self.text):
            return ""  # EOF
        c = self.text[self.pos]
        self.pos += 1
        return c

    def ungetc(self):
        if self.pos > 0:
            self.pos -= 1


def _is_word_char(c):
    return c != "" and (c.isalnum() or c == "_")


def getword(reader, lim=MAXWORD):
    """Fetch next word or single character. Returns None at EOF."""
    c = reader.getchar()
    if c == "":
        return None

    word = [c]
    # not alphanumeric / underscore / hash: return it as a single token
    if not (c.isalnum() or c == "_" or c == "#"):
        return c

    while len(word) < lim - 1:
        c = reader.getchar()
        if not _is_word_char(c):
            if c != "":
                reader.ungetc()  # push the boundary back to the input
            break
        word.append(c)
    return "".join(word)


def get_line_rest(reader, lim=MAXWORD):
    """Skip blanks and capture the remainder of a #define line. Returns None if empty."""
    c = reader.getchar()
    while c in (" ", "\t"):
        c = reader.getchar()

    if c in ("", "\n"):
        return None

    buf = [c]
    while len(buf) < lim - 1:
        c = reader.getchar()
        if c in ("", "\n"):
            break
        buf.append(c)
    return "".join(buf)


def main():
    print("--- K&R Macro Preprocessor Running Mini-Simulation ---")
    print("Type lines of code below. Example:")
    print("  #define MAX 100")
    print("  #define GREETING Hello_World")
    print("  MAX points to GREETING\n")

    reader = CharReader(sys.stdin.read())
    out = sys.stdout

    while True:
        word = getword(reader)
        if word is None:
            break

        if word == "#define":
            # 1. read the macro name (skip the separating whitespace)
            name = getword(reader)
            while name is not None and name in (" ", "\t"):
                name = getword(reader)
            if name is not None and name[0].isalpha():
                # 2. read the rest of the line as the macro value
                defn = get_line_rest(reader)
                if defn is not None:
                    install(name, defn)
        elif word[0].isalpha():
            np = lookup(word)
            out.write(np.defn if np is not None else word)
        else:
            # pass symbols, whitespace and newlines straight through
            out.write(word)

    free_table()


if __name__ == "__main__":
    main()
