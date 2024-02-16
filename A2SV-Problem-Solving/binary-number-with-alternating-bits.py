class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        prev = -1

        while n > 0:
            cur = 1 if n & 1 == 1 else 0
            if prev == cur:
                return False
            prev = cur
            n >>= 1
        return True