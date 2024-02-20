class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {}

        def dp(idx):
            if idx == 0:
                return 0
            if idx == 1 or idx == 2:
                return 1

            if idx not in memo:
                memo[idx] = dp(idx-1) + dp(idx-2) + dp(idx-3)
            
            return memo[idx]

        return dp(n)