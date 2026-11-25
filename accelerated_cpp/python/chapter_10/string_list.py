# Exercises 10-4/10-5: a minimal list of strings that manages its own
# fixed-size storage, reallocating on every push_back/pop_back like the
# C++ version does with new[]/delete[].


class StringList:
    def __init__(self):
        self._values = []   # treated as a fixed-size array
        self._length = 0

    def size(self):
        return self._length

    def push_back(self, s):
        new_values = [None] * (self._length + 1)
        new_values[:self._length] = self._values[:self._length]
        new_values[self._length] = s
        self._values = new_values
        self._length += 1

    def pop_back(self):
        if self._length == 0:
            raise IndexError("pop_back on empty StringList")
        self._length -= 1
        ret = self._values[self._length]
        self._values = self._values[:self._length]
        return ret

    # iterator support (exercise 10-5): forward and reverse traversal
    def __iter__(self):
        for i in range(self._length):
            yield self._values[i]

    def __reversed__(self):
        for i in range(self._length - 1, -1, -1):
            yield self._values[i]

    def __getitem__(self, i):
        if not 0 <= i < self._length:
            raise IndexError(i)
        return self._values[i]
