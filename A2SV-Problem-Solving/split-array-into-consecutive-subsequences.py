class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        last = defaultdict(list)

        for num in nums:
            if last[num - 1]:
                heappush(last[num], heappop(last[num - 1]) + 1)
            else:
                heappush(last[num], 1)

        return all(
            num >= 3
            for tail in last.values()
            for num in tail
        )