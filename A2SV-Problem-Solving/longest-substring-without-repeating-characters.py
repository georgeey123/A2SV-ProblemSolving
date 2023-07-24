class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        visited = set()
        left = 0

        for right in range(len(s)):
            while s[right] in visited:
                visited.remove(s[left])
                left += 1
            visited.add(s[right])
            longest = max(longest, right - left + 1)

        return longest
