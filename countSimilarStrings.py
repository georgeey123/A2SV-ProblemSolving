class Solution:
    def similarPairs(self, words: List[str]) -> int:
        wordMap = {}

        for word in words:
            curr = sorted(set(word))
            curr = ''.join(curr)

            if curr in wordMap:
                wordMap[curr]+=1
            else:
                wordMap[curr]=1
        pairs = 0
       
        for word in wordMap:
            count = wordMap[word]
            pairs += (count* (count-1))//2

        return pairs
