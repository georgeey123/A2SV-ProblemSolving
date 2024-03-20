class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        running_sum = 0
        
        prefix = defaultdict(int)
        prefix[0] = 1
        

        for num in nums:
            running_sum += num
            if (running_sum % k) in prefix:
                count += prefix[running_sum % k]
            prefix[running_sum % k] += 1
        
        return count