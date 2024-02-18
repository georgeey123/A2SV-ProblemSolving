class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        hashmap = defaultdict(int)
        power = len(nums)

        for i in range(2**power):
            subset=0
            for j in range(power):
                if i & (1<<j):
                    subset|=nums[j]
            hashmap[subset]+=1
        return hashmap[max(hashmap)]