"""
String class (port of string_prata.cpp -- S. Prata, C++ Primer Plus 6th ed.,
Programming Exercise 12.2).

Implements: count of live objects (HowMany), has(), stringlow(), stringup(),
operator+ (String+String, char*+String, String+char*), comparisons, [] and
stream input (limited to CINLIM characters).
"""
import sys


class String:
    num_strings = 0
    CINLIM = 80

    def __init__(self, s=""):
        if isinstance(s, String):  # copy constructor
            s = s._str
        self._str = list(s)
        String.num_strings += 1

    def __del__(self):
        String.num_strings -= 1

    @staticmethod
    def HowMany():
        return String.num_strings

    def length(self):
        return len(self._str)

    def has(self, ch):
        # NOTE: the original C++ ignores its argument and always counts 'A';
        # we count the requested character.
        return sum(1 for c in self._str if c == ch)

    def stringlow(self):
        self._str = list("".join(self._str).lower())

    def stringup(self):
        self._str = list("".join(self._str).upper())

    # operator= (String or const char*)
    def assign(self, s):
        self._str = list(s._str if isinstance(s, String) else s)
        return self

    def __getitem__(self, i):
        return self._str[i]

    def __setitem__(self, i, c):
        self._str[i] = c

    # friends
    def __lt__(self, other):
        return str(self) < str(other)

    def __gt__(self, other):
        return str(self) > str(other)

    def __eq__(self, other):
        return str(self) == str(other)

    __hash__ = None

    def __str__(self):
        return "".join(self._str)

    def __add__(self, other):
        return String(str(self) + str(other))

    def __radd__(self, other):
        return String(str(other) + str(self))


def read_string(st):
    """operator>>: read a line (at most CINLIM-1 chars). Returns False on EOF."""
    line = sys.stdin.readline()
    if not line:
        return False
    st.assign(line.rstrip("\n")[:String.CINLIM - 1])
    return True


# main code harness:
def main():
    s1 = String(" and I am a C++ student.")
    s2 = String("Please enter your name: ")
    s3 = String()
    print(s2, end="", flush=True)
    read_string(s3)
    s2 = "My name is  " + s3
    print(f"{s2}.")
    s2 = s2 + s1
    s2.stringup()
    print(f"The string\n{s2}\ncontains {s2.has('A')} 'A' characters in it.")
    s1.assign("red")
    rgb = [String(s1), String("green"), String("blue")]
    print("Enter the name of a primary coler for mixing light: ", end="", flush=True)
    ans = String()
    success = False
    while read_string(ans):
        ans.stringlow()
        for color in rgb:
            if ans == color:
                print("That's right!")
                success = True
                break
        if success:
            break
        else:
            print("Try again!")
    print("Bye")


if __name__ == "__main__":
    main()
