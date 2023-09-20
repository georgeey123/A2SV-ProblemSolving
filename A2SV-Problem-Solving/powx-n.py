class Solution:
    def myPow(self, x: float, n: int) -> float:
        def exp(x,n):
            if n == 0:
                return 1
            if x == 0:
                return 0
                
            res = exp(x, n//2)
            res = res * res
            return x * res if n % 2 else res

        res = exp(x,abs(n))
        return res if n > 0 else 1/res
        