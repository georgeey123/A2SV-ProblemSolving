class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def construct(n):
            if n == 0:
                return [1]

            prev_row = construct(n-1)
            row = [1]
            for i in range(1, n):
                row.append(prev_row[i-1] + prev_row[i])

            row.append(1)

            return row

        res = construct(rowIndex)

        return res