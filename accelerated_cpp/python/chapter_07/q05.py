# Chapter 7, exercise 5: grammar program using linked lists.
# Python's list replaces std::list here; the recursion is the same.
from grammar import bracketed, nrand, read_grammar


def gen_aux(g, word, ret):
    if not bracketed(word):
        ret.append(word)
        return
    if word not in g:
        raise LookupError("empty rule")
    c = g[word]
    r = c[nrand(len(c))]
    for w in r:
        gen_aux(g, w, ret)


def gen_sentence(g):
    ret = []
    gen_aux(g, "<sentence>", ret)
    return ret


def main():
    print(" ".join(gen_sentence(read_grammar())))


if __name__ == "__main__":
    main()
