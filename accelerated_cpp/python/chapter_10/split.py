# Exercise 10-6: split returning a StringList.
from string_list import StringList


def split(s):
    ret = StringList()
    for word in s.split():
        ret.push_back(word)
    return ret
