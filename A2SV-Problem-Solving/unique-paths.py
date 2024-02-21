class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # row = [1] * n

        # for i in range(m-1):
        #     newRow = [1] * n
        #     for j in range(n-2, -1, -1):
        #         newRow[j] = newRow[j+1] + row[j]
        #     row = newRow
        # return row[0] 
        # row = [0] * n

        # for i in range(m):
        #     newRow = [0] * n
        #     print(newRow)

        grid = [[0] * n for _ in range(m)]
        print(grid)
        
        memo = {}

        def dp(row, col):
            if row == m-1 or col == n-1:
                return 1
            if row == m or col == n:
                return 0

            state = (row, col)
            if (row, col) not in memo:
                right = dp(row, col + 1)
                down = dp(row+1, col)
                memo[state] = right + down

            return memo[state]

        return dp(0,0)
