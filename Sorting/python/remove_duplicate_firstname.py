"""
Given a list of names <first_name, last_name>, remove entries with duplicate first
names (the last name doesn't matter).

Solution:
    Sort by first name, then do one traversal removing duplicate first names.

    TC: O(n log n)
    SC: O(1) extra
"""
from dataclasses import dataclass
from itertools import groupby


@dataclass
class Name:
    first: str
    last: str


def remove_first_name_duplicates(names):
    if not names:
        return names

    # 1. Sort primarily by first name so duplicates group together
    names.sort(key=lambda n: (n.first, n.last))

    # 2. Linear traversal deduplication
    write_idx = 0
    for i in range(1, len(names)):
        if names[write_idx].first != names[i].first:  # a fresh, new first name
            write_idx += 1
            names[write_idx] = names[i]

    # Slice and return the unique segment
    return names[:write_idx + 1]


def remove_first_name_duplicates_pythonic(names):
    """Alternative (like std::unique): use itertools.groupby on the sorted list."""
    names = sorted(names, key=lambda n: n.first)
    return [next(group) for _, group in groupby(names, key=lambda n: n.first)]


def print_names(names):
    for n in names:
        print(n.first, n.last)


if __name__ == "__main__":
    names = [Name("jon", "snow"), Name("sam", "khanna"), Name("jon", "oliver"),
             Name("ravi", "snow"), Name("ravi", "raju")]

    print("Deduplicated Names:")
    print_names(remove_first_name_duplicates(list(names)))
