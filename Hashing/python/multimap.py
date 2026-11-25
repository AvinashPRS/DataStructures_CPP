"""
Storing multiple values under the same key.

A plain dict (like std::map) only allows one value per key - assigning to the
same key overwrites the old value. To store multiple values per key:

1. dict[str, list[str]]  (the pattern used in the grammar programs),
   conveniently built with collections.defaultdict(list).
2. A "multimap": Python has no built-in one, but a sorted list of (key, value)
   pairs plus bisect gives the same equal_range behaviour as std::multimap.
"""
import bisect
from collections import defaultdict


def main():
    # =========================================================
    # APPROACH 1: dict with a list as the value
    # (best when you want to pick random items by index, like c[0])
    # =========================================================
    grouped_map = defaultdict(list)

    grouped_map["<noun>"].append("cat")
    grouped_map["<noun>"].append("dog")
    grouped_map["<noun>"].append("table")

    grouped_map["<verb>"].append("jumps")
    grouped_map["<verb>"].append("sits")

    print("=== Approach 1: dict[str, list[str]] ===")
    if "<noun>" in grouped_map:
        values = grouped_map["<noun>"]
        print(f"Key: <noun> has {len(values)} values:")
        for val in values:
            print(f"  - {val}")

    # =========================================================
    # APPROACH 2: multimap emulation
    # (stores separate key-value pairs that share the same key)
    # =========================================================
    multi_map = []  # sorted list of (key, value); insertion order kept for equal keys

    def mm_insert(key, value):
        # bisect on the key only so equal keys keep insertion order (like std::multimap)
        keys = [k for k, _ in multi_map]
        multi_map.insert(bisect.bisect_right(keys, key), (key, value))

    def equal_range(key):
        keys = [k for k, _ in multi_map]
        return bisect.bisect_left(keys, key), bisect.bisect_right(keys, key)

    mm_insert("<noun>", "cat")
    mm_insert("<noun>", "dog")
    mm_insert("<noun>", "table")

    mm_insert("<verb>", "jumps")
    mm_insert("<verb>", "sits")

    print("\n=== Approach 2: multimap (sorted list of pairs) ===")
    lo, hi = equal_range("<noun>")
    print(f"Key: <noun> has {hi - lo} entries:")
    for k, v in multi_map[lo:hi]:
        print(f"  Key: {k} -> Value: {v}")


if __name__ == "__main__":
    main()
