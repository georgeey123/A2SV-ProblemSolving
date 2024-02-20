class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def dp(idx):
            if idx >= len(nums):
                return 0

            if idx not in memo:
                memo[idx] = max(nums[idx] + dp(idx+2), dp(idx+1))

            return memo[idx]

        return dp(0)