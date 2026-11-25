"""
Book Translation: translate a book from English into every target language, using
translators (bidirectional, with a cost). Each target must be reached with the minimum
number of translation steps; among those, pick the cheapest last-hop translator.
Print the total cost, or "Impossible".

Input (stdin):
    num_targets num_translators
    target_lang_1 ... target_lang_n
    from_lang to_lang cost      (num_translators lines)
"""
import sys


def find_distances(adj_list, num_langs):
    # BFS by levels from English (index 0)
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

        # for each newly reached language, the cheapest edge coming from the previous level
        for added_lang in new_positions:
            best = -1
            for to_lang, cost in adj_list[added_lang]:
                if min_moves[to_lang] + 1 == min_moves[added_lang] and (best == -1 or cost < best):
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


# main code harness:
if __name__ == "__main__":
    tokens = sys.stdin.read().split()
    num_targets, num_translators = int(tokens[0]), int(tokens[1])
    idx = 2
    lang_names = ["English"] + tokens[idx:idx + num_targets]
    idx += num_targets
    lang_index = {name: i for i, name in enumerate(lang_names)}

    adj_list = [[] for _ in range(num_targets + 1)]
    for _ in range(num_translators):
        frm, to, cost = tokens[idx], tokens[idx + 1], int(tokens[idx + 2])
        idx += 3
        fi, ti = lang_index[frm], lang_index[to]
        # the C version prepends to a linked list, so newest edges come first
        adj_list[fi].insert(0, (ti, cost))
        adj_list[ti].insert(0, (fi, cost))

    solve(num_targets + 1, find_distances(adj_list, num_targets + 1))
