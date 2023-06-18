class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        
        left = 0
        right = 0

        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
            i += 1

        while right < len(nums):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1

        return nums
