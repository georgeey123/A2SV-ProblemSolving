class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)

        if total % p == 0:
            return 0
        
        prefix = [0] * (len(nums) + 1)

        for i in range(1, len(nums)+1):
            prefix[i] = prefix[i-1] + nums[i-1]

        ans = len(nums)
        print(prefix)
        hashmap = {}

        for i in range(len(prefix)):
            hashmap[(prefix[i]%p)] = i
            if ((prefix[i]%p) - (total % p))%p  in hashmap:
                ans = min(ans, i - hashmap[((prefix[i]%p) - (total % p))%p]) 

        return ans if ans < len(nums) else -1