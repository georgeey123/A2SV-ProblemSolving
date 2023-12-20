class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        graph2 = {i:[] for i in range(len(graph))}
        in_degree = defaultdict(int)

        for rel in range(len(graph)):
            for neighbours in graph[rel]:
                graph2[neighbours].append(rel)
        print(graph2)

        for key in graph2.keys():
            in_degree[key] += len(graph[key])
        print(in_degree)

        queue = deque([key for key, val in in_degree.items() if val == 0])
        res = []
        print(queue, res)
        while queue:
            current = queue.popleft()

            for safe in graph2[current]:
                in_degree[safe] -= 1
                if in_degree[safe] == 0:
                    queue.append(safe)
                    
            res.append(current)
            
        res.sort()
        return res