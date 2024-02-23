class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {}

        def dp(cur_sum):
            if cur_sum in memo:
                return memo[cur_sum]
                
            if cur_sum == target:
                return 1
          
            res = 0
            if cur_sum not in memo:
                for num in nums:
                    if cur_sum <= target:
                        new_sum = num+cur_sum
                        res += dp(new_sum)
                memo[cur_sum] = res 
            return memo[cur_sum]

        return dp(0) 

            