class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected_sum = int(n*(n+1)/2)
        sum = 0

        for num in nums:
            sum += num
        missing_number = expected_sum - sum

        return missing_number
