class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        bounds = int(sqrt(c))

        for a in range(bounds + 1):
            b = sqrt(c-(a*a))
            if b == int(b):
                return True
        return False