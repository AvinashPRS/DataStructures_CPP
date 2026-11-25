"""
K&R (section 6.6) table lookup: a fixed-size hash table with separate chaining.

  - hash:    hash value for a string
  - lookup:  look for s in hashtab
  - install: put (name, defn) in hashtab (overwrites existing defn)
  - undef:   Exercise 6-5, remove a name and definition from the table
"""

HASHSIZE = 101


class NList:
    """Node inside a bucket list."""

    def __init__(self, name, defn, next_node=None):
        self.next = next_node  # next entry in chain
        self.name = name       # defined name (key)
        self.defn = defn       # replacement text (value)


# the central bucket array
hashtab = [None] * HASHSIZE


def hash_str(s):
    """Form hash value for string s (mimics unsigned 32-bit overflow)."""
    hashval = 0
    for ch in s:
        hashval = (ord(ch) + 31 * hashval) & 0xFFFFFFFF
    return hashval % HASHSIZE


def lookup(s):
    np = hashtab[hash_str(s)]
    while np is not None:
        if np.name == s:
            return np  # found
        np = np.next
    return None  # not found


def install(name, defn):
    np = lookup(name)
    if np is None:  # not found: push a new node at the head of the bucket
        hashval = hash_str(name)
        np = NList(name, defn, hashtab[hashval])
        hashtab[hashval] = np
    else:  # already there: replace definition
        np.defn = defn
    return np


def undef(name):
    """Remove a name and definition from the table. Returns 1 if removed, else 0."""
    hashval = hash_str(name)
    prev = None
    np = hashtab[hashval]
    while np is not None:
        if np.name == name:
            if prev is None:
                hashtab[hashval] = np.next  # node at the head of the bucket list
            else:
                prev.next = np.next         # node inside / at the end of the list
            return 1
        prev, np = np, np.next
    return 0


def free_table():
    for i in range(HASHSIZE):
        hashtab[i] = None


if __name__ == "__main__":
    install("MAX", "100")
    install("PI", "3.14159")
    install("STATUS", "SUCCESS")

    # overwrite an existing definition
    install("MAX", "200")

    for key in ("MAX", "PI", "MIN"):
        item = lookup(key)
        if item is not None:
            print(f"Found definition -> {item.name}: {item.defn}")
        else:
            print(f"Key '{key}' is not defined.")

    print(f"undef('PI') -> {undef('PI')}, lookup('PI') -> {lookup('PI')}")
    free_table()
