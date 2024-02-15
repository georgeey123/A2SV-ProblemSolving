class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # n = max(x, y).bin_length

        # for i in range(max(x,y)):


        num = x ^ y
        res = 0

        while num:
            if num & 1 == 1:
                res += 1
            num >>= 1

        return res