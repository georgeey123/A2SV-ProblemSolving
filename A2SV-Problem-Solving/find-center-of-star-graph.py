class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        graph = defaultdict(list)


        for start, end in edges:
            graph[start].append(end)
            graph[end].append(start)

        for i in graph.items():
            if len(i[1]) > 1:
                return i[0]
 