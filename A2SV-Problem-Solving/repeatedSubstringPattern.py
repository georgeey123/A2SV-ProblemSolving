class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)

        for i in range(n//2, 0, -1):
            if n % i == 0:
                repeats = n//i
                sub_string = s[0:i]
                new_string = ""
                for j in range(repeats):
                    new_string += sub_string
                if new_string == s:
                    return True

        return False

  '''
  Time complexity: O(n^2)
  Space complexity: O(n)
  '''
