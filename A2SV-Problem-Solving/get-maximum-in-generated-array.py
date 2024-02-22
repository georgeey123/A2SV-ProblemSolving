class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        nums = [-1] * (n+1)

        # def dp(i):
        #     if i < 2:
        #         nums[i] = i
        #         return nums[i]

        #     if nums[i] == -1:
        #         if i % 2 == 0:
        #             nums[i] = dp((i)//2)
        #         else:
        #             nums[i] = dp((i-1)//2) + dp((i-1)//2 + 1)

        #     return nums[i]

        # for i in range(n, -1, -1):
        #     dp(i)
        # return max(nums)

        dp = [-1] * (n + 1)

        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1 

        dp[0] = 0
        dp[1] = 1

        for i in range(2, n + 1):
            if dp[i] == -1:
                if i % 2 == 0:
                    dp[i] = dp[i // 2]
                else:
                    dp[i] = dp[i // 2] + dp[(i // 2) + 1]

        return max(dp)

