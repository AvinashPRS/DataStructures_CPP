# Grammar reading and random selection helpers from §7.4.
import random
import sys

RAND_MAX = 32767


def read_grammar(stream=sys.stdin):
    """§7.4.2/131: each line is `<category> word word ...`."""
    ret = {}
    for line in stream.read().splitlines():
        entry = line.split()
        if entry:
            ret.setdefault(entry[0], []).append(entry[1:])
    return ret


def bracketed(s):
    """§7.4.3/132"""
    return len(s) > 1 and s[0] == "<" and s[-1] == ">"


def rand():
    return random.randint(0, RAND_MAX)


def nrand(n):
    """§7.4.4/135: random integer in [0, n) using bucketing."""
    if n <= 0 or n > RAND_MAX:
        raise ValueError("Argument to nrand is out of range")
    bucket_size = RAND_MAX // n
    while True:
        r = rand() // bucket_size
        if r < n:
            return r
