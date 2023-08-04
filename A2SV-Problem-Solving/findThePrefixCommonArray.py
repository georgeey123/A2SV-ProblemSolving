class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        res, frequency = [], [0] * (len(A) + 1)
        n, count = len(A), 0

        for i in range(n):
            frequency[A[i]] += 1
            if frequency[A[i]] == 2:
                count += 1
            frequency[B[i]] += 1
            if frequency[B[i]] == 2:
                count += 1
            res.append(count)

        return res
      
'''
Time: O(n)
Space: O(n)
'''
