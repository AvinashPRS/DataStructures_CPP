import heapq

# Uses Dijkstra's Algorithm to find the Shortest Path from an arbitrary vertex to all other vertices.
# Since this version is implemented using a min-priority queue, the time complexity is O((V + E) log V).

INF = float("inf")
NUM_VERTICES = 6  # 6 vertices (0,1,2,3,4,5)


def create_and_add_edge(adj_list, u, weight, v):
    adj_list[u].append((weight, v))  # (weight, vertex)


def dijkstras_algorithm(adj_list, source):
    visited_vertex = [False] * NUM_VERTICES
    shortest_path = [INF] * NUM_VERTICES  # Initialize everything to +infinity
    shortest_path[source] = 0  # Set source distance to zero

    pq = [(0, source)]  # Source has weight 0
    while pq:
        weight, u = heapq.heappop(pq)  # Use to get minimum weight
        if visited_vertex[u]:  # Check for cycle
            continue  # Already accounted for it, move on
        visited_vertex[u] = True  # Mark the vertex so that we won't have to visit it again

        for w, v in adj_list[u]:
            if weight + w < shortest_path[v]:  # Check if we can do better
                shortest_path[v] = weight + w  # Update new distance
                heapq.heappush(pq, (shortest_path[v], v))
    return shortest_path


# Driver function - main code harness:
if __name__ == "__main__":
    source = 0
    adj_list = [[] for _ in range(NUM_VERTICES)]
    create_and_add_edge(adj_list, 0, 5, 1)
    create_and_add_edge(adj_list, 0, 10, 3)
    create_and_add_edge(adj_list, 1, 2, 2)
    create_and_add_edge(adj_list, 1, 10, 5)
    create_and_add_edge(adj_list, 1, 5, 4)
    create_and_add_edge(adj_list, 2, 1, 3)
    create_and_add_edge(adj_list, 2, 5, 4)
    create_and_add_edge(adj_list, 2, 3, 0)
    create_and_add_edge(adj_list, 4, 2, 5)

    # Apply the Dijkstra algorithm now:
    sp = dijkstras_algorithm(adj_list, source)
    print(f"Shortest path from source vertex {source}:", " ".join(str(d) for d in sp))
