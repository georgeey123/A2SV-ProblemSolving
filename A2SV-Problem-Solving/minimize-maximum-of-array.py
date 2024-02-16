class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        def feasible(m):
            total = 0
            for i in range(len(nums)):
                total+=nums[i]
                if m*(i+1) < total:
                    return False
            return True

        l = nums[0]
        r = max(nums)
        target = sum(nums)
        while l < r:
            m = (l+r)//2
            if feasible(m):
                r = m
            else:
                l = m+1
        return l
        