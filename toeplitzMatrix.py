class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for row_idx in range(len(matrix)):
            for col_idx in range(len(matrix[0])):
                if row_idx + 1< len(matrix) and col_idx + 1 < len(matrix[row_idx]) and matrix[row_idx +1][col_idx+1] != matrix[row_idx][col_idx]:
                    return False
        return True
