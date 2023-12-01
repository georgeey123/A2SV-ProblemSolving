class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = defaultdict(list)
        rows, cols = len(isConnected), len(isConnected[0])

        for i in range(rows):
            for j in range(cols):
                if isConnected[i][j] == 1:
                    graph[i+1].append(j+1)

        visited = set()
        def dfs(node, visited):
            if node in visited:
                return False

            visited.add(node)
            for neighbour in graph[node]:
                if neighbour not in visited:
                    a = dfs(neighbour, visited)
                    if a:
                        return a

        count = 0
        for start in graph:
            if dfs(start, visited) == None:
                count += 1

        return count