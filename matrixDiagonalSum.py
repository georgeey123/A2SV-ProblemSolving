class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        res = 0
        for row in range(n):
            res += mat[row][row]
            res += mat[row][n - 1 - row]
        if n & 1:
            res -= mat[n // 2][n // 2]
        
        return res
