from collections import Counter

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        hashmap = Counter()
        last_occurrance = set()

        for c in s:
            hashmap[c] = 1 + hashmap.get(c, 0)

        for c in s:
            if c not in last_occurrance:
                while stack and stack[-1] > c and hashmap[stack[-1]] > 0:
                    last_occurrance.remove(stack.pop())
                stack.append(c)
                last_occurrance.add(c)
            hashmap[c] -= 1
        
        return "".join(stack)
