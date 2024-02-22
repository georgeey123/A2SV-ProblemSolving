class Solution:
    def tribonacci(self, n: int) -> int:
        # memo = {}

        # def dp(idx):
        #     if idx == 0:
        #         return 0
        #     if idx == 1 or idx == 2:
        #         return 1

        #     if idx not in memo:
        #         memo[idx] = dp(idx-1) + dp(idx-2) + dp(idx-3)
            
        #     return memo[idx]

        # return dp(n)

        dp = [0] * (n+1)
        
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1

        dp[0], dp[1], dp[2] = 0, 1, 1

        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

        return dp[-1]