"""Book Translation: BFS for fewest translation steps, then cheapest edge."""
import sys


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
    lang_names = ["English"] + [next(tokens) for _ in range(num_targets)]
    adj_list = [[] for _ in range(num_targets + 1)]
    for _ in range(num_translators):
        from_lang = next(tokens)
        to_lang = next(tokens)
        cost = int(next(tokens))
        from_index = lang_names.index(from_lang)
        to_index = lang_names.index(to_lang)
        adj_list[from_index].insert(0, (to_index, cost))
        adj_list[to_index].insert(0, (from_index, cost))
    min_costs = find_distances(adj_list, num_targets + 1)
    solve(num_targets + 1, min_costs)


if __name__ == "__main__":
    main()
