class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        diff = [0] * (n+2)
        m = len(diff)

        for left, right, direction in shifts:
            if direction == 0:
                diff[left+1] -= 1
                diff[right+2] +=1
            else:
                diff[left+1] += direction 
                diff[right+2] -= direction
        res = []
        for i in range(1, m-1):
            diff[i] += diff[i-1]
            res.append(diff[i])
        print(diff,res)
        ans = ""
        for i in range(len(res)):
            ans += chr(((ord(s[i])-ord('a')+res[i])%26)+ord('a'))

        return ans