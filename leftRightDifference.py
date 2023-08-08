class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        right_sum = sum(nums)
        n = len(nums)
        
        left_sum = 0
        res = []

        for i in range(n):
            right_sum -= nums[i]
            res.append(abs(left_sum - right_sum))
            left_sum += nums[i]

        return res
