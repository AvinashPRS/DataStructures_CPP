"""
Given a list of elements, where a number occurs more than floor(n/2) times. Find this
majority element.

Input: list of numbers
Output: int

Solution (Boyer-Moore voting):
    The count of majority element will be greater than n/2. If we count it up and decrement
    the count for every element that is not the majority, we still end up with at least 1.

    Start with the first element as the majority candidate. If the next element is the same,
    ++count, else --count. If count becomes zero, make the current element the candidate.

TC: O(n)
"""


def find_majority_element(arr):
    c = 0
    majority = arr[0]

    for num in arr:
        if num == majority:
            c += 1
        else:
            c -= 1

        # if count is zero, then change the majority element
        if c <= 0:
            c = 1
            majority = num

    return majority


if __name__ == "__main__":
    arr = [1, 1, 233, 1, 9, 1, 9, 1]
    print(find_majority_element(arr))
