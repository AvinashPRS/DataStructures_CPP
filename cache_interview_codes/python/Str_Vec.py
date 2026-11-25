"""
Str implemented on top of Vec<char> (port of Str_Vec.h / Str_Vec.cpp).

In C++ this version stores its characters in a `Vec<char>` instead of
managing a raw char* buffer itself.
"""
from Vec import Vec


class Str:
    def __init__(self, *args):
        """
        Str()          -> empty
        Str(n, c)      -> n copies of c
        Str("text")    -> from a string
        Str(iterable)  -> from a range (Q10)
        """
        if len(args) == 0:
            self._data = Vec()
        elif len(args) == 2:
            self._data = Vec(args[0], args[1])
        else:
            self._data = Vec()
            for c in args[0]:
                self._data.push_back(c)

    def __getitem__(self, i):
        return self._data[i]

    def __setitem__(self, i, c):
        self._data[i] = c

    def size(self):
        return self._data.size()

    def __iadd__(self, s):
        for c in s:
            self._data.push_back(c)
        return self

    def __add__(self, other):
        r = Str(self)
        r += other
        return r

    # Q12
    def begin(self):
        return self._data.begin()

    def end(self):
        return self._data.end()

    def __iter__(self):
        return iter(self._data)

    # Q12
    def insert(self, d, src):
        return self._data.insert(d, src)

    # operator<<
    def __str__(self):
        return "".join(self._data)


# main code harness:
def main():
    s = Str("Hello, world!")
    print(s)

    # copy the first 5 characters
    msg = "".join(s[i] for i in range(5))
    print(msg)


if __name__ == "__main__":
    main()
