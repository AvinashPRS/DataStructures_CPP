"""Compound Words: print words that are a concatenation of two other words."""
import sys

NUM_BITS = 17


def hashmask(n):
    return (1 << n) - 1


def oaat(key, bits):
    """One-at-a-time hash (emulating 64-bit unsigned arithmetic)."""
    mask64 = (1 << 64) - 1
    h = 0
    for ch in key:
        h = (h + ord(ch)) & mask64
        h = (h + (h << 10)) & mask64
        h ^= h >> 6
    h = (h + (h << 3)) & mask64
    h ^= h >> 11
    h = (h + (h << 15)) & mask64
    return h & hashmask(bits)


def in_hash_table(hash_table, find):
    word_code = oaat(find, NUM_BITS)
    for word in hash_table[word_code]:
        if word == find:
            return True
    return False


def identify_compound_words(words, hash_table):
    for word in words:
        length = len(word)
        for j in range(1, length):
            if in_hash_table(hash_table, word[:j]) and \
                    in_hash_table(hash_table, word[j:]):
                print(word)
                break


def main():
    hash_table = [[] for _ in range(1 << NUM_BITS)]
    words = []
    for line in sys.stdin:
        word = line.rstrip("\n")
        if not word:
            break
        words.append(word)
        hash_table[oaat(word, NUM_BITS)].insert(0, word)
    identify_compound_words(words, hash_table)


if __name__ == "__main__":
    main()
