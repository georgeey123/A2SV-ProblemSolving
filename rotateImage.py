class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        left, right = 0, len(matrix) -1

        while left < right:
            for i in range(right - left):
                top, bottom = left, right
                #save topleft in temp variable
                top_left = matrix[top][left + i]

                #move bottomleft to topleft
                matrix[top][left + i] = matrix[bottom - i][left]
                #move bottomright to bottomleft
                matrix[bottom - i][left] = matrix[bottom][right - i]
                #move topright to bottomright
                matrix[bottom][right - i] = matrix[top + i][right]
                #move topleft in temp variable to topright
                matrix[top + i][right] = top_left

            left += 1
            right -= 1


