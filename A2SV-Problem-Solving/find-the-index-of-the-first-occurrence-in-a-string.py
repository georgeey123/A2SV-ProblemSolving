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
# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:
#         m = (10**9)+7
#         a = 31
#         n = len(needle)
        
#         needle_hash = 0
#         hay_hash = 0
        
#         for i in range(n):
#             needle_hash += ((ord(needle[i]) - ord('a') +1) * (a**(n-i-1)))%m
#             hay_hash += ((ord(haystack[i]) - ord('a') +1) *( a**(n-i-1)))%m

#         if needle_hash == hay_hash:
#             return 0  
            
#         print(needle_hash, hay_hash)
        
#         for j in range(n, len(haystack)):
#             hay_hash -= (ord(haystack[j-n]) - ord('a')+1) * (a**(n-1))
#             hay_hash %= m
#             hay_hash *= a
#             hay_hash += ((ord(haystack[j]) -ord('a')+1))%m
#             hay_hash %= m
            
#             if needle_hash == hay_hash:
#                 return j-n+1

                
#         return -1

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        def hash(string):
            res = 0
            for i in range(len(string)):
                res += (ord(string[i]) - 96) * (26 ** (n-i-1))
            return res % ((10 ** 9)+7)  

        def add(char, code):
            code *= 26
            code += (ord(char)-96)
            return code % ((10 ** 9)+7)

        def remove(char, code):
            code -= (26 ** (n-1)) * (ord(char) - 96)
            return code % ((10 ** 9)+7)

        m, n = len(haystack), len(needle)
        temp = hash(haystack[:n])
        target = hash(needle)
        if temp == target:
            return 0


        for i in range(n, m):
            temp = remove(haystack[i-n], temp)
            temp = add(haystack[i], temp)

            if temp == target:
                return (i-n+1)

        return -1
