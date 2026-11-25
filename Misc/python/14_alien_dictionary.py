"""Find the order of characters in an alien language (topological sort)."""

MAX_NUM_CHARACTERS = 256


def topological_sort_helper(cur_char, adjacency_table, is_visited, s):
    if is_visited[ord(cur_char)]:
        return
    # set is_visited here so that we don't run into loops
    is_visited[ord(cur_char)] = True
    for neighbor_char in adjacency_table[ord(cur_char)]:
        if not is_visited[ord(neighbor_char)]:
            topological_sort_helper(neighbor_char, adjacency_table, is_visited, s)
    # Push only after all characters reachable from it are on the stack
    s.append(cur_char)


def topological_sort(adjacency_table):
    is_visited = [False] * MAX_NUM_CHARACTERS
    s = []
    for i in range(MAX_NUM_CHARACTERS):
        if adjacency_table[i]:
            topological_sort_helper(chr(i), adjacency_table, is_visited, s)
    # Popping the stack gives the order of characters
    while s:
        print(s.pop())


def get_alphabet_order(words):
    """words: the words present in the alien dictionary, in sorted order."""
    adjacency_table = [[] for _ in range(MAX_NUM_CHARACTERS)]
    # Go through consecutive pairs of words
    for word1, word2 in zip(words, words[1:]):
        for a, b in zip(word1, word2):
            # First mismatching position gives an edge a -> b
            if a != b:
                adjacency_table[ord(a)].append(b)
                break
    topological_sort(adjacency_table)


def run_test(words):
    print("Dictionary: " + "".join(f"{w} " for w in words))
    print("Order of characters:")
    get_alphabet_order(words)
    print("_____________________________")


def main():
    run_test(["aaa", "abc", "acb", "dad"])
    run_test(["aba", "abb", "abd", "ac", "ad", "pq"])
    print("Test passed")


if __name__ == "__main__":
    main()
