class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        prefix = 1
        N = len(nums)
        for i in range(N):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(N -1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res 
 
