"""
Bidirectional Dijkstra Shortest Path Algorithm
(https://www.coursera.org/learn/algorithms-on-graphs/lecture/7ml18/bidirectional-dijkstra)

Author: Marinovsky (http://github.com/Marinovsky)

This is basically the same Dijkstra Algorithm but faster because it goes from the source to the
target and from the target to the source and stops when finding a vertex already visited by the
direct search or the reverse one.
Simulation: https://www.youtube.com/watch?v=DINCL5cd_w0&t=24s
"""
import heapq

INF = float("inf")


def add_edge(adj1, adj2, u, v, w):
    """Adds edge u -> v (1-indexed) to the direct graph adj1 and v -> u to the reversed graph adj2."""
    adj1[u - 1].append((v - 1, w))
    adj2[v - 1].append((u - 1, w))


def shortest_path_distance(workset, distance):
    """Shortest distance from source to target given the processed vertices.
    distance[0] = distances from the source, distance[1] = distances from the target."""
    best = INF
    for i in workset:
        best = min(best, distance[0][i] + distance[1][i])
    return best


def bidijkstra(adj1, adj2, s, t):
    """Returns the shortest distance from s to t (0-indexed), or -1 if unreachable."""
    n = len(adj1)
    dist = [[INF] * n, [INF] * n]
    # pq[0]: min heap for the direct search, pq[1]: min heap for the reverse search
    pq = [[(0, s)], [(0, t)]]
    dist[0][s] = 0
    dist[1][t] = 0
    adjs = (adj1, adj2)
    workset = []         # vertices processed by either search
    visited = [False] * n

    while True:
        for side in (0, 1):  # 0 = direct search, 1 = reversed search
            # If the heap is empty, the target is not reachable
            if not pq[side]:
                return -1
            current_dist, current_node = heapq.heappop(pq[side])

            # for all vertices reachable from the current vertex, try to minimise the distance
            for nxt, w in adjs[side][current_node]:
                if current_dist + w < dist[side][nxt]:
                    dist[side][nxt] = current_dist + w
                    heapq.heappush(pq[side], (dist[side][nxt], nxt))

            workset.append(current_node)  # store the processed vertex

            # check if current_node has already been visited by the other search
            if visited[current_node]:
                d = shortest_path_distance(workset, dist)
                return -1 if d == INF else d
            visited[current_node] = True


def tests():
    print("Initiatinig Predefined Tests...")
    print("Initiating Test 1...")
    a1, a2 = [[] for _ in range(4)], [[] for _ in range(4)]
    add_edge(a1, a2, 1, 2, 1)
    add_edge(a1, a2, 4, 1, 2)
    add_edge(a1, a2, 2, 3, 2)
    add_edge(a1, a2, 1, 3, 5)
    assert bidijkstra(a1, a2, 0, 2) == 3
    print("Test 1 Passed...")

    print("Initiating Test 2...")
    assert bidijkstra(a1, a2, 3, 2) == 5
    print("Test 2 Passed...")

    b1, b2 = [[] for _ in range(5)], [[] for _ in range(5)]
    for u, v, w in [(1, 2, 4), (1, 3, 2), (2, 3, 2), (3, 2, 1), (2, 4, 2),
                    (3, 5, 4), (5, 4, 1), (2, 5, 3), (3, 4, 4)]:
        add_edge(b1, b2, u, v, w)
    print("Initiating Test 3...")
    assert bidijkstra(b1, b2, 0, 4) == 6
    print("Test 3 Passed...")
    print("All Test Passed...\n")


# main code harness:
if __name__ == "__main__":
    tests()  # running predefined tests
    vertices = int(input("Enter the number of vertices : "))
    edges = int(input("Enter the number of edges : "))
    adj1 = [[] for _ in range(vertices)]
    adj2 = [[] for _ in range(vertices)]
    print("Enter the edges by three integers in this form: u v w ")
    print("Example: if there is and edge between node 1 and node 4 with weight 7 enter: 1 4 7, and then press enter")
    for k in range(edges):
        u, v, w = map(int, input().split())
        add_edge(adj1, adj2, u, v, w)
        if k != edges - 1:
            print("Enter the next edge")
    print("Enter the source node and the target node separated by a space")
    print("Example: If the source node is 5 and the target node is 6 enter: 5 6 and press enter")
    s, t = map(int, input().split())
    d = bidijkstra(adj1, adj2, s - 1, t - 1)
    if d == -1:
        print("Target not reachable from source")
    else:
        print("Shortest Path Distance :", d)
