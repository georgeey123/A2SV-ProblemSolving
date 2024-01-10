class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)

        i = 0
        while i < n:
            if nums[i] != i + 1:
                if nums[nums[i] - 1] != nums[i]:    
                    nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
                else: 
                    i += 1
            else:
                i += 1

        duplicates = [nums[i] for i in range(n) if nums[i] != i + 1]

        return duplicates