# Code taken from §6.1.3/106-108: find URLs in a string.

URL_CH = "~;/?:@=&$-_.+!*'(),"
SEP = "://"


def not_url_char(c):
    return not (c.isalnum() or c in URL_CH)


def url_end(s, b):
    """Index of the first character at or after b that can't be in a URL."""
    e = len(s)
    while b != e and not not_url_char(s[b]):
        b += 1
    return b


def url_beg(s, b):
    """Index of the start of the next URL at or after b, or len(s)."""
    e = len(s)
    i = s.find(SEP, b)
    while i != -1:
        # make sure the separator isn't at the beginning or end of the line
        if i != b and i + len(SEP) != e:
            beg = i
            while beg != b and s[beg - 1].isalpha():
                beg -= 1
            # at least one appropriate character before and after the separator?
            if beg != i and not not_url_char(s[i + len(SEP)]):
                return beg
        i = s.find(SEP, i + len(SEP))
    return e


def find_urls(s):
    ret = []
    b, e = 0, len(s)
    while b != e:
        b = url_beg(s, b)
        if b != e:
            after = url_end(s, b)
            ret.append(s[b:after])
            b = after
    return ret
