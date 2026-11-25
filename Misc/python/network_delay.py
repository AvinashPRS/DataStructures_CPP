"""Network Delay Time (LeetCode 743) using Dijkstra's algorithm."""
import heapq

INF = float("inf")


class Solution:
    def computeDistance(self, graph, source):
        dist = [INF] * len(graph)
        dist[source] = 0
        pq = [(0, source)]  # min-heap of (distance, vertex)
        while pq:
            current_distance, current_vertex = heapq.heappop(pq)
            if current_distance > dist[current_vertex]:
                continue  # outdated entry
            for neighbor, weight in graph[current_vertex]:
                new_distance = current_distance + weight
                if new_distance < dist[neighbor]:
                    dist[neighbor] = new_distance
                    heapq.heappush(pq, (new_distance, neighbor))
        return dist

    def networkDelayTime(self, times, N, K):
        graph = [[] for _ in range(N)]
        # Build directed graph (nodes are 1-indexed in the input)
        for frm, to, weight in times:
            graph[frm - 1].append((to - 1, weight))
        distance = self.computeDistance(graph, K - 1)
        if any(d == INF for d in distance):
            return -1
        return max(distance)


def main():
    """
        2 ----1----> 1
        |
        1
        v
        3 ----1----> 4

    Starting node: 2 -> network delay = 2
    """
    times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
    result = Solution().networkDelayTime(times, 4, 2)
    print(f"Network delay time: {result}")


if __name__ == "__main__":
    main()
