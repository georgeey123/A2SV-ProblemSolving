class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_avg = float('-inf')
        window_sum = sum(nums[:k])

        for i in range(k, len(nums)):
            avg = window_sum / k
            max_avg = max(max_avg, avg)
            window_sum += nums[i] - nums[i-k]

        max_avg = max(max_avg, window_sum / k)
        return max_avg
