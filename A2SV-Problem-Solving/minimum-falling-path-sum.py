class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        def inbound(i):
            if 0 <= i < len(matrix):
                return True
        @cache
        def dp(row, col):
            if not inbound(row):
                return 0
            if not inbound(col):
                return float('inf')

            # dirs = [[1, -1], [1, 0], [1,1]]

            # cost = float('inf')
            # state = (row, col)
            # if state not in memo:
            #     for direction in dirs:
            diag_left = dp(row+1, col - 1) 
            down = dp(row + 1, col)
            diag_right = dp(row+1, col+1)

            return min(diag_left, down, diag_right) + matrix[row][col]

        res = float('inf')
        for i in range(len(matrix)):
            res = min(res, dp(0,i))
        return res

        # return dp(0, 0)

        # dp = [0] * len(matrix) 

 
