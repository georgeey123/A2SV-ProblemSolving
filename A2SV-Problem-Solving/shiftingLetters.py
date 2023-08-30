class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:

        n = len(shifts)
        prefix_sum = [0] * (n + 1)
        for i in range(n-1, -1, -1):
            prefix_sum[i] = prefix_sum[i+1] + shifts[i]

        print(prefix_sum)
        output = ""

        for i in range(n):
            offset = (ord(s[i]) - 97 + (prefix_sum[i])) % 26 + 97
            output += chr(offset)
            
        return output
