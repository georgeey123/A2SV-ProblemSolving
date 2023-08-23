class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left, right = 0, 0
        res, zero_count = 0, 0

        while right < len(nums):
            if nums[right] == 0:
                zero_count += 1
            
            while zero_count == 2:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            res = max(res, right - left)
            right += 1

        return res

  '''
  Time complexity: O(n) - size of array
  Space complexity: O(1) - constant extra space used (res, zero_count)

  approach:
Initialize two pointers, left and right, both starting at 0.
Initialize a variable res to store the maximum subarray length.
Initialize a variable zero_count to count the number of zeroes encountered.
Iterate through the array using the right pointer.
If the element at index right is 0, increment zero_count.
Inside the loop, keep moving the left pointer until zero_count becomes 1 again.
While moving the left pointer, decrement zero_count if the element at index left is 0.
Update res with the maximum of res and the difference between right and left.
Increment the right pointer to expand the window.
Return the final value of res as the result.
  '''
