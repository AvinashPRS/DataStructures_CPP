from collections import deque

INF = float("inf")


class Solution:
    def find_cheapest_price(self, n, flights, src, dst, k):
        # 1. Build adjacency list: u -> (v, price)
        adj = [[] for _ in range(n)]
        for u, v, price in flights:
            adj[u].append((v, price))

        # 2. Track minimum cost to reach each node
        min_cost = [INF] * n
        min_cost[src] = 0

        # 3. BFS Queue stores: (stops, current_node, current_cost)
        q = deque([(0, src, 0)])
        while q:
            stops, u, cost = q.popleft()

            # If we have exceeded K stops, we cannot move further from this node
            if stops > k:
                continue

            # Traverse all neighboring flights
            for v, price in adj[u]:
                # Relaxation condition: if a cheaper price is found, update and push to queue
                if cost + price < min_cost[v]:
                    min_cost[v] = cost + price
                    q.append((stops + 1, v, min_cost[v]))

        # Return the min cost to destination, or -1 if unreachable within K stops
        return -1 if min_cost[dst] == INF else min_cost[dst]


# main code harness:
if __name__ == "__main__":
    solver = Solution()
    flights = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
    result = solver.find_cheapest_price(4, flights, 0, 3, 1)
    print("Cheapest flight price:", result)  # Output: 700
