"""
Random sentence generator using a grammar (recursive version).

Grammar = dict[str, list[Rule]], Rule = list[str]
gen_aux recursively expands bracketed categories, so words appear in the right order.
"""
import io
import random

GRAMMAR_DATA = (
    "<noun> cat\n"
    "<noun> dog\n"
    "<noun> table\n"
    "<noun-phrase> <noun>\n"
    "<noun-phrase> <adjective> <noun-phrase>\n"
    "<adjective> large\n"
    "<adjective> brown\n"
    "<adjective> absurd\n"
    "<verb> jumps\n"
    "<verb> sits\n"
    "<location> on the stairs\n"
    "<location> under the sky\n"
    "<location> wherever it wants\n"
    "<sentence> the <noun-phrase> <verb> <location>\n"
)


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


def gen_aux(g, word, ret):
    if not bracketed(word):
        ret.append(word)
    else:
        if word not in g:
            raise LookupError("empty rule")
        c = g[word]
        r = c[nrand(len(c))]
        # recurse
        for w in r:
            gen_aux(g, w, ret)


def gen_sentence(g):
    ret = []
    gen_aux(g, "<sentence>", ret)
    return ret


if __name__ == "__main__":
    g = read_grammar(io.StringIO(GRAMMAR_DATA))

    # generate and print 3 random sentences
    for _ in range(3):
        print(" ".join(gen_sentence(g)) + ".")
