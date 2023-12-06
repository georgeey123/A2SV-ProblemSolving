class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for start, end in dislikes:
            graph[start].append(end)
            graph[end].append(start)

        color = {}
        visited = set()

        def dfs(node, c):
            if node in color:
                return color[node] == c

            color[node] = c

            for neighbor in graph[node]:
                if not dfs(neighbor, -c):
                    return False

            return True

        for node in range(1, n + 1):
            if node not in color and not dfs(node, 1):
                return False

        return True
