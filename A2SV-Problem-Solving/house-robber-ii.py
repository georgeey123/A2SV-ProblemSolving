class Solution:
    # def helper(self, nums):
    #         rob1, rob2 = 0, 0

    #         for n in nums:
    #             new_rob = max(rob1 + n, rob2)
    #             rob1 = rob2
    #             rob2 = new_rob
    #         return rob2

    # def rob(self, nums: List[int]) -> int:

    #     return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        def dp(idx, nums, memo):
            if idx >= len(nums):
                return 0

            if idx not in memo:
                memo[idx] = max(nums[idx] + dp(idx+2, nums, memo), dp(idx+1, nums, memo))

            return memo[idx]

        return max(nums[0], dp(0, nums[1:], {}), dp(0, nums[:-1], {}))