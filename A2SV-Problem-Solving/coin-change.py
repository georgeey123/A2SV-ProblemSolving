class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # memo = {}

        # def dp(i):
        #     if i == 0:
        #         return 0
        #     if i < 0:
        #         return float('inf')

        #     mn = float('inf')

        #     if i not in memo:
        #         for coin in coins:
        #             mn = min(mn, 1 + dp(i-coin))
        #             memo[i] = mn
        #     return memo[i]

        # res = dp(amount)

        # return res if res != float('inf') else -1

        dp = [amount + 1] * (amount+1)
        dp[0] = 0

        for i in range(1, len(dp)):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], 1 + dp[i-coin])

        res = dp[amount]

        return res if res != amount + 1 else -1