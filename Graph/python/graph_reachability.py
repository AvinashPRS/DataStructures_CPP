"""
Problem: Given an array consisting of outcomes for matches played between pairs of teams.
Two teams A and B have been given; find whether we can arrange the teams in such a way that
the series starts with A and ends with B and each team in the series has beaten the team that
comes after it in the series. The outcome is either: win or loss

Input: Array of outcomes, team A, team B
Output: bool

Solution:
    This is a reachability problem where we know the source and sink. We just need to check
    whether there is a path from A to B or not. We can use either DFS or BFS for this.

TC: O(E), E: no. of edges
"""
from collections import defaultdict, deque
from dataclasses import dataclass


@dataclass
class MatchResults:
    winner: str
    loser: str


# build the graph: edge (u, v) where u is the winning team and v is the losing team
def build_graph(matches):
    g = defaultdict(set)
    for m in matches:
        g[m.winner].add(m.loser)
    return dict(g)


def is_reachable_dfs(g, curr, dest, visited):
    # if the dest node has been reached
    if curr == dest:
        return True
    # if the current node has no edges or has already been visited
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
        # check if the dest has been reached or not
        if curr == dest:
            return True
        # push all the adjacent unvisited nodes
        for node in g.get(curr, ()):
            if node not in visited:
                visited.add(node)
                q.append(node)
    return False


def is_possible_path(matches, A, B, method):
    g = build_graph(matches)
    if method == "DFS":
        return is_reachable_dfs(g, A, B, set())
    elif method == "BFS":
        return is_reachable_bfs(g, A, B, set())
    raise ValueError("method must be 'DFS' or 'BFS'")


def print_graph(g):
    for k, v in g.items():
        print(f"{k}: " + " ".join(v))


# main code harness:
if __name__ == "__main__":
    matches = [MatchResults(*p) for p in
               [("A", "C"), ("C", "D"), ("C", "E"), ("D", "A"), ("E", "D"), ("B", "D")]]
    print_graph(build_graph(matches))
    print(int(is_possible_path(matches, "A", "B", "DFS")))
    print(int(is_possible_path(matches, "A", "B", "BFS")))
