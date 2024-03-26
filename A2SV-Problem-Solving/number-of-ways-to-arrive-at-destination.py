class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)

        for u, v, w in roads:
            graph[u].append((v, w))
            graph[v].append((u, w))

        times = [float('inf')] * n
        times[0] = 0

        ways = [0] * n
        ways[0] = 1

        heap = [(0, 0)]

        while heap:
            cost, node = heapq.heappop(heap)

            for v, w in graph[node]:
                new_cost = cost + w
                if new_cost < times[v]:
                    heapq.heappush(heap, (new_cost, v))
                    times[v] = new_cost
                    ways[v] = ways[node]
                elif new_cost == times[v]:
                    ways[v] += ways[node]

        mod = 10**9 + 7

        return ways[-1] % mod



