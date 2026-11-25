"""
Dijkstra's algorithm (min-priority queue): shortest path from a source vertex
to all other vertices. O(V + E log V).

Also includes (from the commented-out part of the C++ file) a longest-path
variant that only works on DAGs; run with --longest to try it.
"""
import heapq
import sys

NUM_VERTICES = 6  # vertices 0..5
INF = 100000


def create_and_add_edge(adj_list, u, weight, v):
    adj_list[u].append((weight, v))


def dijkstras_algorithm(adj_list, source):
    visited_vertex = [False] * NUM_VERTICES
    shortest_path = [INF] * NUM_VERTICES
    shortest_path[source] = 0
    pq = [(0, source)]  # (distance, vertex) min-heap

    while pq:
        weight, u = heapq.heappop(pq)
        if visited_vertex[u]:
            continue  # already accounted for
        visited_vertex[u] = True
        for w, v in adj_list[u]:
            if weight + w < shortest_path[v]:  # can we do better?
                shortest_path[v] = weight + w
                heapq.heappush(pq, (shortest_path[v], v))
    return shortest_path


def longest_path_algorithm(adj_list, source):
    """Max-path variant; works ONLY on directed acyclic graphs."""
    longest = [None] * NUM_VERTICES  # None = -infinity
    longest[source] = 0
    pq = [(0, source)]  # max-heap via negated weights
    while pq:
        neg_w, u = heapq.heappop(pq)
        if -neg_w < longest[u]:
            continue  # outdated entry
        for w, v in adj_list[u]:
            if longest[v] is None or longest[u] + w > longest[v]:
                longest[v] = longest[u] + w
                heapq.heappush(pq, (-longest[v], v))
    return longest


def build_graph(with_cycle_edge=True):
    adj_list = [[] for _ in range(NUM_VERTICES)]
    create_and_add_edge(adj_list, 0, 5, 1)
    create_and_add_edge(adj_list, 0, 10, 3)
    create_and_add_edge(adj_list, 1, 2, 2)
    create_and_add_edge(adj_list, 1, 10, 5)
    create_and_add_edge(adj_list, 1, 5, 4)
    create_and_add_edge(adj_list, 2, 1, 3)
    create_and_add_edge(adj_list, 2, 5, 4)
    if with_cycle_edge:
        # creates cycle 0->1->2->0, so it is left out for longest path
        create_and_add_edge(adj_list, 2, 3, 0)
    create_and_add_edge(adj_list, 4, 2, 5)
    return adj_list


def main():
    source = 0
    if "--longest" in sys.argv:
        longest = longest_path_algorithm(build_graph(False), source)
        print(f"Longest path from source vertex {source}: " +
              "".join("INF " if d is None else f"{d} " for d in longest))
        return
    shortest = dijkstras_algorithm(build_graph(), source)
    print(f"Shortest path from source vertex {source}: " +
          "".join(f"{d} " for d in shortest))


if __name__ == "__main__":
    main()
