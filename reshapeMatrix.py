class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r * c != len(mat) * len(mat[0]):
            return mat

        row, col = len(mat), len(mat[0])

        trans_mat = []
        current = []

        for i in range(row):
            for j in range(col):
                current.append(mat[i][j])
                if len(current) == c:
                    trans_mat.append(current)
                    current = []

        return trans_mat
