class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        ranges.sort()
        res, bundles = 1, [float('-inf')]

        for start, end in ranges:
            if start <= bundles[-1]:
                bundles[-1] = max(bundles[-1], end)
            else:
                res = (res * 2) % (10 ** 9 + 7)
                bundles = [start, end]
        return res
