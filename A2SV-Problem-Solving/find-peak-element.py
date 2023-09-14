class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        peek = 0
        left, right = 0,  len(nums) - 1
        nums.append(float('-inf'))

        if len(nums) <= 1:
            return 0

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] > nums[mid -1] and nums[mid] > nums[mid + 1]:
                peek = mid
                return peek
            elif nums[mid] < nums[mid - 1] or nums[mid] > nums[mid+1]:
                right = mid - 1
            elif nums[mid] > nums[mid - 1] or nums[mid] < nums[mid+1]:
                left = mid + 1

        return right+1