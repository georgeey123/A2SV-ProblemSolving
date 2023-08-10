class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seq_map = set(nums)
        longest = 0

        for n in nums:
            if (n-1) not in seq_map:
                length = 0
                while (n + length) in seq_map:
                    length += 1
                longest =max (length, longest)
        return longest
