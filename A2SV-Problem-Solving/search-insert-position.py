class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # return bisect_left(nums, target)
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = left + (right-left) // 2
            
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
        return left
