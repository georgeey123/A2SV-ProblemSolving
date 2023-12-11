class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        if grid[0][0] == 1:
            return -1

        n = len(grid)
        visited = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, - 1), (1, 1), (-1, 1), (1, -1), (-1, -1)]

        def is_valid(r, c):
            row_inbound = 0 <= r < n
            col_inbound = 0 <= c < n
            return row_inbound and col_inbound and grid[r][c] == 0

        source = (0, 0, 1)
        queue = deque([source])
        visited.add((0, 0))

        while queue:
            r, c, length = queue.popleft()

            if r == c == (n - 1):
                return length

            for dr, dc in directions:
                if is_valid(dr + r, dc + c) and (dr + r, dc + c) not in visited:
                    visited.add((dr + r, dc + c))
                    queue.append((r + dr, c + dc, length + 1))
        return -1



        