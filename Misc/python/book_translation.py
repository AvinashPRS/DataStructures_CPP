"""
                             Book Translation
DMOJ problem ecna16d

You want a book translated into n target languages. You've found m translators.
Each knows how to translate between two languages for a given cost c. Reaching
a target language may require multiple translations (e.g. English -> Spanish ->
Bengali). Minimise the number of translations to each target language; among
those, choose the one with minimum total cost.

Input: one test case:
    1. A line with 2 integers n and m (target languages, translators).
    2. A line containing n strings naming the target languages (English is the
       starting language and will not be among them).
    3. m lines: language1 language2 cost. At most one translator per pair.

Output: the minimum cost to translate the book into all target languages while
minimising the number of translations to each, or "Impossible".

Note: the C version links the reverse edge into adj_list[from_index] (a bug);
here the reverse edge goes to adj_list[to_index] as intended.
"""
import sys


def find_lang(langs, lang):
    return langs.index(lang)


def find_distances(adj_list, num_langs):
    min_moves = [-1] * num_langs
    min_costs = [-1] * num_langs
    min_moves[0] = 0
    cur_positions = [0]

    while cur_positions:
        new_positions = []
        for from_lang in cur_positions:
            for to_lang, _cost in adj_list[from_lang]:
                if min_moves[to_lang] == -1:
                    min_moves[to_lang] = 1 + min_moves[from_lang]
                    new_positions.append(to_lang)

        for added_lang in new_positions:
            best = -1
            for to_lang, cost in adj_list[added_lang]:
                if min_moves[to_lang] + 1 == min_moves[added_lang] and \
                        (best == -1 or cost < best):
                    best = cost
            min_costs[added_lang] = best

        cur_positions = new_positions
    return min_costs


def solve(num_langs, min_costs):
    total = 0
    for i in range(1, num_langs):
        if min_costs[i] == -1:
            print("Impossible")
            return
        total += min_costs[i]
    print(total)


def main():
    tokens = iter(sys.stdin.read().split())
    num_targets = int(next(tokens))
    num_translators = int(next(tokens))
    print(f"num_targets: {num_targets}\nnum_translators: {num_translators}")  # debug

    lang_names = ["English"] + [next(tokens) for _ in range(num_targets)]
    for name in lang_names[1:]:  # debug
        print(name)

    adj_list = [[] for _ in range(num_targets + 1)]
    for _ in range(num_translators):
        from_lang = next(tokens)
        to_lang = next(tokens)
        cost = int(next(tokens))
        from_index = find_lang(lang_names, from_lang)
        to_index = find_lang(lang_names, to_lang)
        adj_list[from_index].insert(0, (to_index, cost))
        adj_list[to_index].insert(0, (from_index, cost))

    min_costs = find_distances(adj_list, num_targets + 1)
    solve(num_targets + 1, min_costs)


if __name__ == "__main__":
    main()
