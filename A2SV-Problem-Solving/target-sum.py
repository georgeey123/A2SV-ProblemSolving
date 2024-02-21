class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def dp(i,cur_sum):
            if i == len(nums):
                return int(cur_sum == target)

            state = (i, cur_sum)

            if state not in memo:
                memo[state] = dp(i+1, nums[i] + cur_sum) + dp(i+1, -nums[i] + cur_sum)

            return memo[state]

        return dp(0,0)