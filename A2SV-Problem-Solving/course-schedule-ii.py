class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i: [] for i in range(numCourses)}
        in_degree = defaultdict(int)

        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)
        print(graph)


        for key, value in graph.items():
            for val in graph[key]:
                in_degree[val] += 1      
        print(in_degree)

        queue = deque([i for i in graph if i not in in_degree])
        print(queue)
        t_sort = []
        while queue:
            current = queue.popleft()

            for neighbour in graph[current]:
                in_degree[neighbour] -= 1
                if in_degree[neighbour] == 0:
                    queue.append(neighbour)
            
            t_sort.append(current)

        return t_sort if len(t_sort) == numCourses else []


