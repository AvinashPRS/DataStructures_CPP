"""Word Ladder (LeetCode 127): build a graph of one-letter-apart words, then BFS."""
from collections import deque


class Solution:
    def __init__(self):
        self.graph = {}     # word -> neighbouring words
        self.distance = {}  # word -> ladder length from beginWord

    @staticmethod
    def has_edge(str1, str2):
        """True if the words differ in exactly one position."""
        if len(str1) != len(str2):
            return False
        diff = 0
        for a, b in zip(str1, str2):
            if a != b:
                diff += 1
                if diff > 1:
                    return False
        return diff == 1

    def build_graph(self, word_list):
        for i in range(len(word_list)):
            for j in range(i + 1, len(word_list)):
                if self.has_edge(word_list[i], word_list[j]):
                    self.graph.setdefault(word_list[i], []).append(word_list[j])
                    self.graph.setdefault(word_list[j], []).append(word_list[i])

    def ladderLength(self, beginWord, endWord, wordList):
        if endWord not in wordList:
            return 0
        wordList.append(beginWord)
        self.build_graph(wordList)

        q = deque([beginWord])
        self.distance[beginWord] = 1
        while q:
            cur_word = q.popleft()
            if cur_word == endWord:
                return self.distance[cur_word]
            for neighbour in self.graph.get(cur_word, []):
                if neighbour in self.distance:
                    continue
                self.distance[neighbour] = self.distance[cur_word] + 1
                q.append(neighbour)
        return 0


def main():
    word_list = ["hot", "dot", "dog", "lot", "log", "cog"]
    result = Solution().ladderLength("hit", "cog", word_list)
    print(f"Shortest ladder length: {result}")


if __name__ == "__main__":
    main()
