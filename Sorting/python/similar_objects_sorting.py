"""
Given a list of records where many share the same age, put records with the same age
together (they need not be sorted, just grouped). The key is the age.

Solution:
    Count occurrences of each distinct key. From the counts, compute the first position
    (offset) each key's group should occupy. Then, in place, repeatedly move the element
    at a group's next free slot to its own group's next free slot (swap), decrementing
    that group's remaining count and advancing its offset. Remove a key once its count
    reaches 0.

    For sorted output, iterate over keys in sorted order when computing offsets.

    TC: O(n)
    SC: O(m), m: distinct keys
"""
from collections import Counter
from dataclasses import dataclass


@dataclass
class Info:
    age: int
    name: str


def bring_similar_together(arr):
    arr = list(arr)

    # count for each distinct age
    age_count = Counter(o.age for o in arr)

    # first position each age group can take in the list
    array_offset = {}
    offset_pos = 0
    for age, count in age_count.items():
        array_offset[age] = offset_pos
        offset_pos += count

    # place the objects at their correct positions
    while array_offset:
        # the next free slot of some group still being filled
        to_pos = next(iter(array_offset.values()))
        # the group that the element currently sitting there belongs to
        curr_age = arr[to_pos].age
        curr_pos = array_offset[curr_age]

        # move that element into its group's next free slot
        arr[to_pos], arr[curr_pos] = arr[curr_pos], arr[to_pos]

        # it is now placed: decrement its count, advance its offset
        age_count[curr_age] -= 1
        array_offset[curr_age] += 1

        # remove the key once its whole group is placed
        if age_count[curr_age] == 0:
            del array_offset[curr_age]

    return arr


if __name__ == "__main__":
    arr = [Info(12, "sam"), Info(16, "ram"), Info(12, "jon"), Info(22, "prince"),
           Info(12, "manish"), Info(22, "audrey"), Info(42, "ramesh")]
    for a in bring_similar_together(arr):
        print(f"{a.name}, {a.age}")
    print()
