class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # memo = {}

        # def dp(idx):
        #     if idx >= len(cost):
        #         return 0

        #     if idx not in memo:
        #         one_step, two_step = dp(idx+1), dp(idx+2)
        #         memo[idx] = cost[idx] + min(one_step, two_step)

        #     return memo[idx]

        # return min(dp(0),dp(1))

        dp = [0] * (len(cost)+1)
        dp[-2] = dp[-3] = cost[-1]

        for i in range(len(cost)-2, -1, -1):
            dp[i] = cost[i] + min(dp[i+1], dp[i+2])

        return min(dp[0], dp[1])

