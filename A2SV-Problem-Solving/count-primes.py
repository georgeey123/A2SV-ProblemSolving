class Solution:
    def countPrimes(self, n: int) -> int:
        if n<3: return 0
        
        sieve = [True] * n
        sieve[0:n:2] = [False] * len(sieve[0:n:2])
        sieve[1], sieve[2] = False, True

        for i in range(3, int(n**0.5)+1):
            if sieve[i]:
                for j in range(i*i, n, i):
                    sieve[j] = False

        return sieve.count(True)