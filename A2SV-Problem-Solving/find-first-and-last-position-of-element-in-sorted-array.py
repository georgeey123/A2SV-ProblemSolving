class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        # first_idx, last_idx = n, n

        left, right = 0, n-1

        def find_first(array, target):
            left, right = 0, n-1
            first_idx = -1

            while left <= right:
                mid = left + (right-left) // 2

                if array[mid] == target:
                    first_idx = mid
                    right = mid - 1
                elif array[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1 
            # if target not in nums:
            #     first_idx = -1
            return first_idx

        def find_last(array, target):
            left, right = 0, n-1
            last_idx = -1

            while left <= right:
                mid = left + (right-left) // 2

                if array[mid] == target:
                    last_idx = mid
                    left = mid + 1
                elif array[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            # if target not in nums:
            #     last_idx = -1
            return last_idx
                    
        return find_first(nums, target), find_last(nums, target)
        

            