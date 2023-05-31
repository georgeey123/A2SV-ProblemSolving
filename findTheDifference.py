class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count_s = Counter(s)
        count_t = Counter(t)
        count_res = count_t - count_s

        for key,val in count_res.items():
            if val == 1:
                return key
