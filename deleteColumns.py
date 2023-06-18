class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs[0])
        result = 0

        for i in range(0, n):
            for j in range (1, len(strs)):
                if strs[j][i] < strs[j-1][i]:
                    result += 1
                    break
        return result
