"""K&R style chained hash table (lookup / install) - section 6.6."""

HASHSIZE = 101


class NList:
    """Table entry."""

    def __init__(self, name, defn, nxt=None):
        self.next = nxt    # next entry in chain
        self.name = name   # defined name (key)
        self.defn = defn   # replacement text (value)


hashtab = [None] * HASHSIZE


def hash_(s):
    """Form hash value for string s (32-bit unsigned arithmetic like C)."""
    hashval = 0
    for ch in s:
        hashval = (ord(ch) + 31 * hashval) & 0xFFFFFFFF
    return hashval % HASHSIZE


def lookup(s):
    np = hashtab[hash_(s)]
    while np is not None:
        if np.name == s:
            return np  # found
        np = np.next
    return None  # not found


def install(name, defn):
    """Put (name, defn) in hashtab; replaces the value if name exists."""
    np = lookup(name)
    if np is None:  # not found, insert at front of chain
        hashval = hash_(name)
        np = NList(name, defn, hashtab[hashval])
        hashtab[hashval] = np
    else:  # already exists: key stays, replace the value
        np.defn = defn
    return np


def display_table():
    print("\n--- Current Hash Table State ---")
    for i in range(HASHSIZE):
        if hashtab[i] is not None:
            line = f"Bucket [{i}]: "
            np = hashtab[i]
            while np is not None:
                line += f"({np.name} -> {np.defn}) "
                np = np.next
            print(line)
    print("--------------------------------\n")


def free_table():
    for i in range(HASHSIZE):
        hashtab[i] = None


def main():
    # 1. Insert initial configurations
    install("MAX_WIDTH", "1920")
    install("MAX_HEIGHT", "1080")
    install("VERSION", "2.4.1")
    install("AUTHOR", "Kernighan & Ritchie")

    # 2. Display inserted values
    display_table()

    # 3. Overwrite an existing configuration key
    print("Updating VERSION to '3.0.0'...")
    install("VERSION", "3.0.0")

    # 4. Query and verify results
    for key in ["VERSION", "MAX_WIDTH", "INVALID_KEY"]:
        result = lookup(key)
        if result is not None:
            print(f"Lookup Success: Key '{result.name}' equals '{result.defn}'")
        else:
            print(f"Lookup Failed: Key '{key}' not found.")

    # 5. Clean up
    free_table()


if __name__ == "__main__":
    main()
