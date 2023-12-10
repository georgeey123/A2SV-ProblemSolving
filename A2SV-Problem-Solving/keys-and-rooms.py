class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        graph = defaultdict(list)
        n = len(rooms)

        for i, lst in enumerate(rooms):
            graph[i] = lst

        def bfs(node):
            visited = set()
            queue = deque([node])
            visited.add(node)

            while queue:
                node = queue.popleft()

                for neighbour in graph[node]:
                    if neighbour not in visited:
                        visited.add(neighbour)
                        queue.append(neighbour)

            return visited

        visited_rooms = bfs(0)

        return len(visited_rooms) == n
