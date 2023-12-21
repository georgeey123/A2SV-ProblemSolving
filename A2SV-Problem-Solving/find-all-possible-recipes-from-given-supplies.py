class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)
        in_degree = defaultdict(int)
        queue = deque()
        res = []

        for recipe in recipes:
            in_degree[recipe] = 0

        for supply in supplies:
            in_degree[supply] = 0

        for recipe in range(len(recipes)):
            for ing in ingredients[recipe]:
                graph[ing].append(recipes[recipe])
                in_degree[recipes[recipe]] += 1

        for val in in_degree:
            if in_degree[val] == 0:
                queue.append(val)

        while queue:
            curr = queue.popleft()
            if curr not in supplies:
                res.append(curr)

            for neighbour in graph[curr]:
                in_degree[neighbour] -= 1

                if in_degree[neighbour] == 0:
                    queue.append(neighbour)


        return res