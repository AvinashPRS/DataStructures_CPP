"""Exercise 6-5: undef removes a name and definition from the table
maintained by lookup and install (hash table with chaining)."""

HASH_SIZE = 101
SIZE_T_MASK = (1 << 64) - 1  # emulate C size_t overflow


class ListNode:
    def __init__(self, name, definition, next_node):
        self.name = name
        self.definition = definition
        self.next = next_node


hash_table = [None] * HASH_SIZE


def hash_(s):
    hash_value = 0
    for ch in s:
        hash_value = (ord(ch) + 31 * hash_value) & SIZE_T_MASK
    return hash_value % HASH_SIZE


def lookup(s):
    node = hash_table[hash_(s)]
    while node is not None:
        if node.name == s:
            return node
        node = node.next
    return None


def install(name, definition):
    node = lookup(name)
    if node is None:
        h = hash_(name)
        node = ListNode(name, definition, hash_table[h])
        hash_table[h] = node
    else:
        node.definition = definition
    return node


def undef(name):
    h = hash_(name)
    prev, node = None, hash_table[h]
    while node is not None:
        if node.name == name:
            if prev is None:
                hash_table[h] = node.next
            else:
                prev.next = node.next
            return True
        prev, node = node, node.next
    return False


def main():
    install("TEST", "test")

    # Install other collision values for the same hash as for "TEST" -> 51.
    install("TSHe", "test1")
    install("UPXD", "test2")
    install("9iww", "test3")
    install("mY1a", "test4")
    install("uuoT", "test5")

    node = lookup("TEST")
    if node is None:
        print("Error: hash value not found.")
    else:
        print("%s: %s" % (node.name, node.definition))
        if undef("TEST") and lookup("TEST") is None:
            print("'%s' was undefined successfully." % "TEST")
        else:
            print("Error: failed to undefine '%s'." % "TEST")


if __name__ == "__main__":
    main()
