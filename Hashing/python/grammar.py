"""
Random sentence generator from a grammar read from stdin (Accelerated C++ §7.4).

Grammar = dict[str, list[Rule]], Rule = list[str]
Each input line: <category> word1 word2 ...

This version expands rules iteratively by inserting the bracketed
sub-rules at the front of a work list.

Example:
    python3 grammar.py < grammar.txt
"""
import random
import sys


def split(s):
    return s.split()


def read_grammar(stream):
    """Read a grammar from a given input stream."""
    ret = {}
    for line in stream:
        entry = split(line)
        if entry:
            # use the category to store the associated rule
            ret.setdefault(entry[0], []).append(entry[1:])
    return ret


def bracketed(s):
    return len(s) > 1 and s[0] == "<" and s[-1] == ">"


def nrand(n):
    """Return a random integer in the range [0, n)."""
    if n <= 0:
        raise ValueError("Argument to nrand is out of range")
    return random.randrange(n)


def gen_sentence(g):
    rules = ["<sentence>"]  # holds the rules still to be expanded
    sentence = []           # holds the generated sentence

    while rules:
        # locate the rule that corresponds to word
        if rules[0] not in g:
            raise LookupError("empty rule")

        c = g[rules[0]]
        r = c[nrand(len(c))]

        # remove the used rule
        rules.pop(0)

        # bracketed words go back to the front of the rules list (in order),
        # plain words go to the sentence
        insert_pos = 0
        for word in r:
            if bracketed(word):
                rules.insert(insert_pos, word)
                insert_pos += 1
            else:
                sentence.append(word)

    return sentence


if __name__ == "__main__":
    sentence = gen_sentence(read_grammar(sys.stdin))
    print(" ".join(sentence))
