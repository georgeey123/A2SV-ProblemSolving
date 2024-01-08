class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        
        i = 0
        while i < n:
            if 0 <= nums[i] < n and nums[i] != nums[nums[i]]:
                nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
            else:
                i += 1

        for i in range(n):
            if nums[i] != i:
                return i

        return n