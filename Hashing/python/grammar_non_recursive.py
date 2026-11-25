"""
Random sentence generator using a grammar (non-recursive / iterative version).

Uses a list as a stack: rule tokens are pushed in REVERSE order so the first
token ends up on top of the stack.
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
        entry = split(line)  # converts the line into a list of words, i.e. a Rule
        if entry:
            ret.setdefault(entry[0], []).append(entry[1:])
    return ret


def bracketed(s):
    return len(s) > 1 and s[0] == "<" and s[-1] == ">"


def nrand(n):
    if n <= 0:
        raise ValueError("Argument to nrand is out of range")
    return random.randrange(n)


def gen_sentence(g):
    sentence = []
    stack = ["<sentence>"]  # start with the root rule on the stack

    while stack:
        word = stack.pop()

        if not bracketed(word):
            # plain word: add it directly to the final sentence
            sentence.append(word)
        else:
            if word not in g:
                raise LookupError("empty rule")
            c = g[word]  # NB: one key can have multiple values
            r = c[nrand(len(c))]
            # push the rule's tokens in reverse so the first token is on top
            stack.extend(reversed(r))

    return sentence


if __name__ == "__main__":
    g = read_grammar(io.StringIO(GRAMMAR_DATA))

    for _ in range(3):
        # every time the loop is run it generates a new sentence
        print(" ".join(gen_sentence(g)) + ".")
