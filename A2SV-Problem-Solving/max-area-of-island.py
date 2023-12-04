class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()

        def dfs(row, col):
            if(row < 0 or row == rows or col < 0 or col == cols or
            grid[row][col] == 0 or (row,col) in visited):
                return 0

            visited.add((row, col))
            return dfs(row-1, col) + dfs(row+1, col) + dfs(row, col-1) + dfs(row, col+1) + 1

        area = 0

        for i in range(rows):
            for j in range(cols):
                area = max(area, dfs(i,j))

        return area