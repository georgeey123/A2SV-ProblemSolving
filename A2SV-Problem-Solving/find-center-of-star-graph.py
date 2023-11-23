class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        graph = defaultdict(list)


        for start, end in edges:
            graph[start].append(end)
            graph[end].append(start)

        def dfs(vertex, visited):
            if vertex in visited:
                return
            if len(graph[vertex]) > 1:
                return vertex

            visited.add(vertex)
            for neighbour in graph[vertex]:
                if dfs(neighbour, visited):
                    return dfs(neighbour, visited)

        return dfs(edges[0][0], set())        
 