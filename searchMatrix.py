class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        m, n = len(matrix), len(matrix[0])
        row, col = 0, 0

        while row < m and col < n:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                return False 
            else:
                col += 1

            if col == n:
                row += 1
                col = 0

        return False    
