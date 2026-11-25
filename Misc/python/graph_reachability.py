"""
Problem: Given the outcomes of matches played between pairs of teams, and two
teams A and B, can we arrange teams in a series that starts with A, ends with
B, and where each team beat the next team in the series?

Solution: a reachability problem - is there a path from A to B in the graph
with an edge winner -> loser? Use DFS or BFS. TC: O(E)

Note: the C++ BFS marks `curr` (instead of the neighbour) as visited and calls
g.at() on nodes that may have no outgoing edges; both are fixed here.
"""
from collections import deque


class MatchResult:
    def __init__(self, winner, loser):
        self.winner = winner
        self.loser = loser


def build_graph(matches):
    """Edge (u, v) where u is the winning team and v the losing team."""
    g = {}
    for match in matches:
        g.setdefault(match.winner, set()).add(match.loser)
    return g


def is_reachable_dfs(g, curr, dest, visited):
    if curr == dest:
        return True
    # no outgoing edges, or already visited
    if curr not in g or curr in visited:
        return False
    visited.add(curr)
    for team in g[curr]:
        if is_reachable_dfs(g, team, dest, visited):
            return True
    return False


def is_reachable_bfs(g, start, dest, visited):
    q = deque([start])
    visited.add(start)
    while q:
        curr = q.popleft()
        if curr == dest:
            return True
        for node in g.get(curr, ()):
            if node not in visited:
                q.append(node)
                visited.add(node)
    return False


def is_possible_path(matches, a, b, method):
    g = build_graph(matches)
    if method == "DFS":
        return is_reachable_dfs(g, a, b, set())
    if method == "BFS":
        return is_reachable_bfs(g, a, b, set())
    return False


def print_graph(g):
    for team, losers in g.items():
        print(f"{team}: " + "".join(f"{x} " for x in losers))


def main():
    matches = [MatchResult("A", "C"), MatchResult("C", "D"), MatchResult("C", "E"),
               MatchResult("D", "A"), MatchResult("E", "D"), MatchResult("B", "D")]
    print_graph(build_graph(matches))
    print(int(is_possible_path(matches, "A", "B", "DFS")))
    print(int(is_possible_path(matches, "A", "B", "BFS")))


if __name__ == "__main__":
    main()
