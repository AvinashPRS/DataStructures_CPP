# Chapter 8, exercise 5 (part 1): gen_sentence writes to an output sink.
# Any callable taking one word acts as the "output iterator".
import io
import sys

from _paths import use_chapter

use_chapter(7)
from grammar import bracketed, nrand, read_grammar  # noqa: E402


def gen_aux(g, word, out):
    if not bracketed(word):
        out(word)
        return
    if word not in g:
        raise LookupError("empty rule")
    c = g[word]
    for w in c[nrand(len(c))]:
        gen_aux(g, w, out)


def gen_sentence(g, out):
    gen_aux(g, "<sentence>", out)


def main():
    gr = read_grammar(io.StringIO(sys.stdin.read()))

    print("result from ostream: ", end="")
    gen_sentence(gr, lambda w: sys.stdout.write(w + " "))
    print()

    sentence = []
    print("result from list: ", end="")
    gen_sentence(gr, sentence.append)
    print(" ".join(sentence))


if __name__ == "__main__":
    main()
