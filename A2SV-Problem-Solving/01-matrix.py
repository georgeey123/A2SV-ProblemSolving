class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]

        visited = set()
        queue = deque()

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    queue.append((i,j))
                else:
                    mat[i][j] = float('inf')

        def inbound(r,c):
            return (0<=r<len(mat) and 0<=c<len(mat[0]))

        while queue:
            r, c = queue.popleft()

            for dr, dc in dirs:
                new_row = dr + r
                new_col = dc + c

                if inbound(new_row, new_col) and (new_row, new_col)not in visited and (mat[r][c] < mat[new_row][new_col]):
                    mat[new_row][new_col] = mat[r][c] + 1
                    queue.append((new_row, new_col))

        return mat