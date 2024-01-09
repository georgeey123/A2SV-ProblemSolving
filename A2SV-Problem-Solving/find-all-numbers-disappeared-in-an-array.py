class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)

        i = 0
        while i < n:
            if 0 <= nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
            else:
                i += 1

        missing_numbers = [i+1 for i in range(n) if nums[i] != i + 1]

        return missing_numbers