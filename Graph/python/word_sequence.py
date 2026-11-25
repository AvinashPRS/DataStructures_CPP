"""
Given a dictionary of words, starting string 's' and target string 't', check if there is a
sequence of words which starts with 's' and ends with 't'. Each adjacent word should differ in
only one position and all words in the sequence should be of the same length. Return the
smallest sequence length, else return -1.

TC: O(n * d * 26), n: string length, d: no. of words in dict
SC: O(d)

We use BFS for finding the shortest distance. The vertex is the word and an edge exists between
two words if they differ by only one character. Instead of creating the graph (O(d^2)), we
generate candidate neighbours of the current word and check whether they are in the dict.
"""
from collections import deque
from string import ascii_lowercase


def find_sequence(dictionary, s, t):
    dictionary = set(dictionary)
    # make the starting word visited and add to queue
    dictionary.discard(s)
    q = deque([(s, 1)])

    while q:
        word, dist = q.popleft()
        if word == t:
            return dist
        # try all the combinations and search if they are there in dict or not
        chars = list(word)
        for i in range(len(chars)):
            original = chars[i]
            for ch in ascii_lowercase:  # tries all the chars at the fixed position i
                chars[i] = ch
                cand = "".join(chars)
                if cand in dictionary:
                    # make the current word visited and add to queue
                    dictionary.discard(cand)
                    q.append((cand, dist + 1))
            chars[i] = original  # revert the word
    return -1


# main code harness:
if __name__ == "__main__":
    d = {"mug", "dug", "jug", "lug", "lag"}
    print(find_sequence(d, "dug", "lag"))  # 3: dug -> lug -> lag
