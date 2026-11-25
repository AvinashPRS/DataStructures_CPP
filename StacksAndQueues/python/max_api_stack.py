"""
Design a stack with max functionality. The stack should be able to return the maximum element in O(1).

Input: numbers for stack
Output: stack with max api

Solution:
    To ensure we know about the max element at every instant, we use another stack. That stack tracks the current max element.
    Basically for every push we see if the current top element is greater than the element being pushed or not, if it is
    then we push, else we don't push it. Since any element which occurs after the current max, for it the max is always
    going to the current max.

    Now for handling duplicates we need to know their count. This can be done in two ways:
    1. Either we use a stack of values i.e max and when we see an element which is equal to the top
       then we push it also, so we can account for duplicates. But if our array has only duplicates then it will
       take O(n).
    2. We use [max, freq] as stack element. The freq part is for keeping count of duplicates. Every time a
       duplicate is popped we just decrement its count and for a new push of a duplicate increment its count. But if we have
       all distinct elements, then we will be using twice the memory compared to way 1.

    TC: O(1) for push, pop, max and is_empty
    SC: O(n), n: no. of elements
"""


class StackWithMaxAPI:
    def __init__(self):
        self._max_tracker = []  # entries are [max, freq]
        self._s = []

    def push(self, data):
        self._s.append(data)

        if not self._max_tracker:
            self._max_tracker.append([data, 1])
        elif self._max_tracker[-1][0] <= data:
            if self._max_tracker[-1][0] == data:
                self._max_tracker[-1][1] += 1
            else:
                self._max_tracker.append([data, 1])

    def pop(self):
        if not self._s:
            raise IndexError("Stack is empty")

        popped_el = self._s.pop()

        if popped_el == self._max_tracker[-1][0]:
            if self._max_tracker[-1][1] > 1:
                self._max_tracker[-1][1] -= 1
            else:
                self._max_tracker.pop()

        return popped_el

    def max(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self._max_tracker[-1][0]

    def is_empty(self):
        return not self._s


if __name__ == "__main__":
    el = StackWithMaxAPI()
    el.push(1.5)
    el.push(4.7)
    el.push(4.7)

    print(f"Current Max: {el.max()}")          # 4.7
    el.pop()
    print(f"Max after one pop: {el.max()}")    # still 4.7 (due to frequency tracker)
    el.pop()
    print(f"Max after two pops: {el.max()}")   # 1.5
