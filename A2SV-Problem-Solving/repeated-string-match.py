class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:

        def solve(new_string):
            s = b + '#' + new_string
            n = len(s)
            m = len(b)            

            lps = [0] * n
            for i in range(1, n):
                j = lps[i-1]

                while j > 0 and s[i] != s[j]:
                    j = lps[j - 1]

                if s[i] == s[j]:
                    j += 1
                
                if j == m:
                    return 1

                lps[i] = j

            return 0

        k = len(b) // len(a)

        for i in range(k, k+3):
            new_string = a * i
            if solve(new_string):
                return i

        return -1