class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums) 
        hash_set = {}
        arr, ans = [0] * (n+1), 0
        count_distinct = 0

        for i in range(1, n+1):
            arr[i] += arr[i-1] + nums[i-1]

        for i in range(k):
            hash_set[nums[i]] = hash_set.get(nums[i], 0) + 1
            if hash_set[nums[i]] == 1:
                count_distinct += 1
        if count_distinct == k:
            ans = max(ans, arr[i+1] - arr[i-k+1])
            
        for i in range(k,n):
            hash_set[nums[i]] = hash_set.get(nums[i], 0) + 1
            if hash_set[nums[i]] == 1:
                count_distinct += 1
            hash_set[nums[i-k]] = hash_set.get(nums[i-k], 0) - 1

            if hash_set[nums[i-k]] == 0:
                count_distinct -= 1
            if count_distinct == k:
                ans = max(ans, arr[i+1] - arr[i-k+1])
        return ans
