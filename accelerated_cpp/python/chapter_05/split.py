# Code taken from §5.6/88: split a line into whitespace-separated words.


def split(s):
    ret = []
    i = 0
    n = len(s)
    # invariant: we have processed characters [original value of i, i)
    while i != n:
        # ignore leading blanks
        while i != n and s[i].isspace():
            i += 1
        # find end of next word
        j = i
        while j != n and not s[j].isspace():
            j += 1
        # if we found some nonwhitespace characters
        if i != j:
            ret.append(s[i:j])
            i = j
    return ret
