class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}

        def dp(idx):
            if idx >= len(cost):
                return 0

            if idx not in memo:
                one_step, two_step = dp(idx+1), dp(idx+2)
                memo[idx] = cost[idx] + min(one_step, two_step)

            return memo[idx]

        return min(dp(0),dp(1))
