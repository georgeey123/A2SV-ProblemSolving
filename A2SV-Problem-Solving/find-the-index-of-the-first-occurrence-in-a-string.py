class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        
        if len(needle) > len(haystack):
            return -1

        # for i in range(len(haystack)+ 1 - len(needle)):
        #     if haystack[i: i + len(needle)] == needle:
        #         return i  
        
        p2 = 0
        for i in range(len(haystack)):
            ans = i
            while i < len(haystack) and haystack[i] == needle[p2]:
                i += 1
                p2 += 1
                
                if p2 == len(needle):
                    return ans
                
            p2 = 0
        
        return -1