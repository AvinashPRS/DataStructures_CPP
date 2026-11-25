import heapq

INF = float("inf")


class PrimMST:
    def find_mst(self, num_vertices, adj):
        # Min-heap to store (edge_weight, destination_node)
        pq = []
        in_mst = [False] * num_vertices      # nodes currently included in the MST
        min_key = [INF] * num_vertices       # min weight to connect a node to the MST
        parent = [-1] * num_vertices         # to reconstruct the MST paths

        # Initialize by pushing the root node (0) with a weight of 0
        start = 0
        heapq.heappush(pq, (0, start))
        min_key[start] = 0
        total = 0

        while pq:
            # Extract the vertex with the minimum edge weight connection
            weight, u = heapq.heappop(pq)
            # Skip processing if the node is already part of the MST
            if in_mst[u]:
                continue
            # Include vertex u into the MST
            in_mst[u] = True
            total += weight

            for v, edge_weight in adj[u]:
                # if v is not yet in MST and this edge is cheaper than the existing connection to v
                if not in_mst[v] and edge_weight < min_key[v]:
                    min_key[v] = edge_weight
                    parent[v] = u
                    heapq.heappush(pq, (edge_weight, v))

        print("Edges in the constructed MST:")
        for i in range(1, num_vertices):
            if parent[i] != -1:
                print(f"{parent[i]} -- {i} == {min_key[i]}")
        print("Minimum Spanning Tree Total Weight:", total)


# main code harness:
if __name__ == "__main__":
    n = 4
    adj = [[] for _ in range(n)]  # adj[u] = list of (neighbor, weight)
    for u, v, w in [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]:
        adj[u].append((v, w))
        adj[v].append((u, w))
    PrimMST().find_mst(n, adj)
