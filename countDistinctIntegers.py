class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        s = set()

        for i in nums:
            s.add(i)
            s.add(int(str(i)[::-1]))

        return len(s)
