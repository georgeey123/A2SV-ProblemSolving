class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [str(i) for i in range(1, n+1)]
        output = []
        factorial = math.factorial(n)
        index = k-1
        
        while nums:
            factorial = factorial // len(nums)
            pos = index // factorial
            candidate = nums.pop(pos)
            output.append(candidate)
            index %= factorial
            
        return "".join(output)