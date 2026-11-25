"""
Random sentence generator whose output goes to an "output iterator".

In C++ the generator was templated on an output iterator (ostream_iterator or
back_inserter). In Python the equivalent is passing a callable that consumes
each generated word (e.g. a print function or list.append).

Example:
    python3 grammar_iterator.py < grammar.txt
"""
import random
import sys


def split(s):
    return s.split()


def read_grammar(stream):
    ret = {}
    for line in stream:
        entry = split(line)
        if entry:
            ret.setdefault(entry[0], []).append(entry[1:])
    return ret


def bracketed(s):
    return len(s) > 1 and s[0] == "<" and s[-1] == ">"


def nrand(n):
    if n <= 0:
        raise ValueError("Argument to nrand is out of range")
    return random.randrange(n)


def gen_aux(g, word, out):
    if not bracketed(word):
        out(word)  # write result to the output "iterator"
    else:
        if word not in g:
            raise LookupError("empty rule")
        c = g[word]
        r = c[nrand(len(c))]
        # recursively expand the selected rule
        for w in r:
            gen_aux(g, w, out)


def gen_sentence(g, out):
    gen_aux(g, "<sentence>", out)


if __name__ == "__main__":
    gr = read_grammar(sys.stdin)

    # generate the sentence writing straight to stdout
    print("result from ostream: ", end="")
    gen_sentence(gr, lambda w: print(w, end=" "))
    print()

    # generate the sentence into a list
    sentence = []
    print("result from list: ", end="")
    gen_sentence(gr, sentence.append)
    print(" ".join(sentence))
