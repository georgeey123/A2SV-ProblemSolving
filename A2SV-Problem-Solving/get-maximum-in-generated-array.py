class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        nums = [-1] * (n+1)
        # nums[0] = 0
        # nums[1] = 1


        def dp(i):
            if i < 2:
                nums[i] = i
                return nums[i]

            if nums[i] == -1:
                if i % 2 == 0:
                    nums[i] = dp((i)//2)
                else:
                    nums[i] = dp((i-1)//2) + dp((i-1)//2 + 1)

            return nums[i]

        for i in range(n, -1, -1):
            dp(i)
        return max(nums)

