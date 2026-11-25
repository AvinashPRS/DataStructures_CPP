"""
Given a weighted, undirected and connected graph with adjacency list adj, find the shortest
distance of all vertices from the source vertex src. The graph has no negative weight edges.

Input: adjList = [[[1, 9]], [[0, 9]]], src = 0
Output: [0, 9]

Input: adjList = [[[1, 1], [2, 6]], [[2, 3], [0, 1]], [[1, 3], [0, 6]]], src = 2
Output: [4, 3, 0]
Explanation: For nodes 2 to 0, we can follow the path 2-1-0 with distance 1+3 = 4, whereas the
path 2-0 has a distance of 6.

Comparison Between Dijkstra's Original PQ Implementation and Modern PQ Implementation:
With the visited array, we ensure that a node is processed exactly once, but it increases memory
usage. Without the visited array, the same node could be stored in the priority queue multiple
times, but the copy with the smaller distance is processed first, so the result is unaffected.
For large sparse graphs where memory is the concern, avoid the visited array; when time is the
concern, skip it for better performance. Overall time and space are the same for both.
Note: total number of edges in dense graphs will never exceed V^2.

What Is Edge Relaxation?
Edge relaxation means checking if going through a specific edge provides a shorter path to a
node. If it does, we update the shortest distance to that node. E.g. you know the shortest
distance to city A; you check if taking the road from A to city B gives a shorter distance to B
than what you already know. If yes, update it. This is called relaxing the edge.
"""
import heapq

INF = float("inf")


class BruteForce:
    # O(V*V) & O(V) : Where V = total nodes.  Preferred for Dense Graphs.
    def shortest_path(self, adj_list, src):
        n = len(adj_list)
        is_visited = [False] * n
        min_distance = [INF] * n  # shortest distance from source to node i
        min_distance[src] = 0

        for _ in range(n):
            # Select the unvisited node with the minimum distance
            node, curr_distance = -1, INF
            for i in range(n):
                if not is_visited[i] and min_distance[i] < curr_distance:
                    curr_distance, node = min_distance[i], i
            if node == -1:
                break  # remaining nodes are unreachable
            is_visited[node] = True

            # Relax the edges
            for neighbor, w in adj_list[node]:
                nd = curr_distance + w
                if not is_visited[neighbor] and min_distance[neighbor] > nd:
                    min_distance[neighbor] = nd
        return min_distance


class OriginalImplementationByPQ:
    # O(E log V) & O(V).  Preferred for Sparse Graphs.
    def dijkstra(self, adj_list, src):
        n = len(adj_list)
        is_visited = [False] * n
        min_distance = [INF] * n
        min_distance[src] = 0
        min_heap = [(0, src)]
        while min_heap:
            curr_distance, node = heapq.heappop(min_heap)
            is_visited[node] = True
            for neighbor, w in adj_list[node]:  # Relax the edges
                nd = curr_distance + w
                if not is_visited[neighbor] and min_distance[neighbor] > nd:
                    min_distance[neighbor] = nd
                    heapq.heappush(min_heap, (nd, neighbor))
        return min_distance


class OriginalIntuitionBySet:
    # O(E log V) & O(V).  Uses an ordered set; Python has none built in, so we emulate
    # std::set with a sorted list (begin() == index 0).  Preferred for Sparse Graphs.
    def dijkstra(self, adj_list, src):
        import bisect
        n = len(adj_list)
        is_visited = [False] * n
        min_distance = [INF] * n
        min_distance[src] = 0
        st = [(0, src)]
        while st:
            curr_distance, node = st.pop(0)
            is_visited[node] = True
            for neighbor, w in adj_list[node]:
                nd = curr_distance + w
                if not is_visited[neighbor] and min_distance[neighbor] > nd:
                    min_distance[neighbor] = nd
                    bisect.insort(st, (nd, neighbor))
        return min_distance


class ModernImplementationByPQ:
    # O(E log V) & O(V).  Preferred for Sparse Graphs.
    def dijkstra(self, adj_list, src):
        n = len(adj_list)
        min_distance = [INF] * n
        min_distance[src] = 0
        min_heap = [(0, src)]
        while min_heap:
            curr_distance, node = heapq.heappop(min_heap)
            for neighbor, w in adj_list[node]:
                nd = curr_distance + w
                if min_distance[neighbor] > nd:
                    min_distance[neighbor] = nd
                    heapq.heappush(min_heap, (nd, neighbor))
        return min_distance


# main code harness (the C++ file had none; added to exercise all four versions):
if __name__ == "__main__":
    examples = [
        ([[(1, 9)], [(0, 9)]], 0, [0, 9]),
        ([[(1, 1), (2, 6)], [(2, 3), (0, 1)], [(1, 3), (0, 6)]], 2, [4, 3, 0]),
    ]
    for adj, src, expected in examples:
        results = {
            "BruteForce": BruteForce().shortest_path(adj, src),
            "OriginalImplementationByPQ": OriginalImplementationByPQ().dijkstra(adj, src),
            "OriginalIntuitionBySet": OriginalIntuitionBySet().dijkstra(adj, src),
            "ModernImplementationByPQ": ModernImplementationByPQ().dijkstra(adj, src),
        }
        for name, r in results.items():
            print(f"{name:28s} src={src}: {r}  (expected {expected})")
