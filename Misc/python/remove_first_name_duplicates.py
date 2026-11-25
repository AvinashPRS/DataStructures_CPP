"""Remove entries with duplicate first names (keep the first after sorting)."""
from functools import total_ordering


@total_ordering
class Name:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __eq__(self, other):
        # equality only looks at the first name (used for de-duplication)
        return self.first_name == other.first_name

    def __lt__(self, other):
        if self.first_name != other.first_name:
            return self.first_name < other.first_name
        return self.last_name < other.last_name


class Solution:
    def EliminateDuplicate(self, names):
        names.sort()
        # like std::unique: keep the first of each run of equal elements
        result = []
        for name in names:
            if not result or not (result[-1] == name):
                result.append(name)
        names[:] = result


def main():
    names = [Name("John", "Smith"), Name("John", "Adams"), Name("Alice", "Brown"),
             Name("Bob", "Clark"), Name("Alice", "Davis")]
    Solution().EliminateDuplicate(names)
    for name in names:
        print(f"{name.first_name} {name.last_name}")


if __name__ == "__main__":
    main()
