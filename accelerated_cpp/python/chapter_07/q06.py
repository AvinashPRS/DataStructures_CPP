# Chapter 7, exercise 6: generate a sentence without recursion, using an
# explicit list of pending rules.
from grammar import bracketed, nrand, read_grammar


def gen_sentence(g):
    rules = ["<sentence>"]
    sentence = []
    while rules:
        word = rules.pop(0)
        if word not in g:
            raise LookupError("empty rule")
        c = g[word]
        r = c[nrand(len(c))]

        insert_at = 0
        for w in r:
            if bracketed(w):
                rules.insert(insert_at, w)
                insert_at += 1
            else:
                sentence.append(w)
    return sentence


def main():
    print(" ".join(gen_sentence(read_grammar())))


if __name__ == "__main__":
    main()
